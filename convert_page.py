from spire.presentation import *
from spire.presentation.common import *

# Create a Presentation object
presentation = Presentation()

# Load a PowerPoint presentation in PPTX/PPT format
presentation.LoadFromFile("data/GenAI Overview.pptx")

slide = presentation.Slides[0]

# Convert the presentation to PDF format
slide.SaveToFile("data/GenAI_Overview_Page_1.pdf", FileFormat.PDF)
presentation.Dispose()