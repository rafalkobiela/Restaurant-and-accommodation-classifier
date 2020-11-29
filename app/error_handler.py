from pandas.errors import ParserError

from app import tag


@tag.errorhandler(Exception)
def handle_errors(e):
    error_code = 500
    if isinstance(e, ParserError):
        error_code = 400
    return {'message': str(e)}, error_code
