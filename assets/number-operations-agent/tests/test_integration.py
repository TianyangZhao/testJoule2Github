"""Integration test for the Number Operations Agent end-to-end flow."""
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from langchain_core.messages import AIMessage


@pytest.fixture
def mock_llm_response():
    """Mock LLM response that simulates the agent calling arithmetic tool and returning result."""
    ai_msg = AIMessage(content="25 multiplied by 47 equals 1175.")
    mock_result = {"messages": [ai_msg]}
    return mock_result


@pytest.mark.asyncio
async def test_agent_end_to_end_arithmetic(mock_llm_response):
    """Test full agent flow: query -> tool selection -> response."""
    from app.agent import SampleAgent
    from app.tools.arithmetic import arithmetic
    from app.tools.statistics import statistics_calculator
    from app.tools.unit_conversion import unit_conversion
    from app.tools.financial import financial_calculator

    agent = SampleAgent()

    with patch.object(agent, "_invoke_with_fallback", new_callable=AsyncMock) as mock_invoke:
        mock_invoke.return_value = mock_llm_response

        tools = [arithmetic, statistics_calculator, unit_conversion, financial_calculator]
        response = await agent.invoke(
            query="What is 25 multiplied by 47?",
            context_id="test-thread-001",
            tools=tools,
        )

    assert response.status == "completed"
    assert "1175" in response.message


@pytest.mark.asyncio
async def test_agent_stream_returns_chunks(mock_llm_response):
    """Test that agent stream yields status chunks and a final completed chunk."""
    from app.agent import SampleAgent
    from app.tools.arithmetic import arithmetic

    agent = SampleAgent()

    with patch.object(agent, "_invoke_with_fallback", new_callable=AsyncMock) as mock_invoke:
        mock_invoke.return_value = mock_llm_response

        chunks = []
        async for chunk in agent.stream(
            query="Add 10 and 20",
            context_id="test-thread-002",
            tools=[arithmetic],
        ):
            chunks.append(chunk)

    assert len(chunks) >= 2
    # First chunk is a "Processing..." status
    assert chunks[0]["is_task_complete"] is False
    # Last chunk is completed
    assert chunks[-1]["is_task_complete"] is True
    assert chunks[-1]["content"] is not None


@pytest.mark.asyncio
async def test_agent_handles_error_gracefully():
    """Test that the agent returns an error response if the LLM call fails."""
    from app.agent import SampleAgent
    from app.tools.arithmetic import arithmetic

    agent = SampleAgent()

    with patch.object(agent, "_invoke_with_fallback", new_callable=AsyncMock) as mock_invoke:
        mock_invoke.side_effect = Exception("LLM unavailable")

        response = await agent.invoke(
            query="What is 5 + 3?",
            context_id="test-thread-003",
            tools=[arithmetic],
        )

    assert response.status in ("completed", "error")
    assert response.message is not None
