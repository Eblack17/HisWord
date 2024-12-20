import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
workers = 4
timeout = 120
accesslog = '-'
errorlog = '-'
capture_output = True
enable_stdio_inheritance = True
