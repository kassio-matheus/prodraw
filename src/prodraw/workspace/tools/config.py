"""Stores configuration and mappings for drawing tools."""

from prodraw.controllers.shapes import circle_bind
from prodraw.controllers.shapes import rectangle_bind
from prodraw.controllers.shapes import oval_bind
from prodraw.controllers.shapes import line_bind
from prodraw.controllers.shapes import freedraw_bind

# Maps UI option strings to their corresponding drawing tool initialization functions
#Is required .unbind() in controller shape on change. -> Coming soon
DRAW_TOOLS = {
    'rectangle': rectangle_bind,
    'circle': circle_bind,
    'oval': oval_bind,
    'line': line_bind,
    'freedraw': freedraw_bind
}
