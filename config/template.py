from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates", autoescape=False, auto_reload=True)
