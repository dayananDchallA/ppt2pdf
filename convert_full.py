from spire.presentation import *
from spire.presentation.common import *

# Create a Presentation object
presentation = Presentation()

# Load a PowerPoint presentation in PPTX/PPT format
presentation.LoadFromFile("data/GenAI Overview.pptx")

# Convert the presentation to PDF format
presentation.SaveToFile("data/GenAI_Overview.pdf", FileFormat.PDF)
presentation.Dispose()