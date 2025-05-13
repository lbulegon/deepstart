from pydantic import Field

from app_openmanus.agent.toolcall import ToolCallAgent
from app_openmanus.config import config
from app_openmanus.prompt.visualization import NEXT_STEP_PROMPT, SYSTEM_PROMPT
from app_openmanus.tool import Terminate, ToolCollection
from app_openmanus.tool.chart_visualization.chart_prepare import VisualizationPrepare
from app_openmanus.tool.chart_visualization.data_visualization import DataVisualization
from app_openmanus.tool.chart_visualization.python_execute import NormalPythonExecute


class DataAnalysis(ToolCallAgent):
    """
    A data analysis agent that uses planning to solve various data analysis tasks.

    This agent extends ToolCallAgent with a comprehensive set of tools and capabilities,
    including Data Analysis, Chart Visualization, Data Report.
    """

    name: str = "DataAnalysis"
    description: str = "An analytical agent that utilizes multiple tools to solve diverse data analysis tasks"

    system_prompt: str = SYSTEM_PROMPT.format(directory=config.workspace_root)
    next_step_prompt: str = NEXT_STEP_PROMPT

    max_observe: int = 15000
    max_steps: int = 20

    # Add general-purpose tools to the tool collection
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            NormalPythonExecute(),
            VisualizationPrepare(),
            DataVisualization(),
            Terminate(),
        )
    )
