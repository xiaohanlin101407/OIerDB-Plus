from django.http import JsonResponse


class QuickJsonResponse_:

    def __call__(self, code, message="") -> dict:
        try:
            code = str(code)
        except ValueError:
            return self(500, f"Unexpected {code} with type {str(type(code))}")

        JsonResponses = {
            '100': 'Continue',
            '101': 'Switching Protocols',
            '200': 'OK',
            '201': 'Created',
            '202': 'Accepted',
            '203': 'Non-Authoritative Information',
            '204': 'No Content',
            '205': 'Reset Content',
            '206': 'Partial Content',
            '300': 'Multiple Choices',
            '301': 'Moved Permanently',
            '302': 'Found',
            '303': 'See Other',
            '304': 'Not Modified',
            '305': 'Use Proxy',
            '306': 'Unused',
            '307': 'Temporary Redirect',
            '400': 'Bad Request',
            '401': 'Unauthorized',
            '402': 'Payment Required',
            '403': 'Forbidden',
            '404': 'Not Found',
            '405': 'Method Not Allowed',
            '406': 'Not Acceptable',
            '407': 'Proxy Authentication Required',
            '408': 'Request Time-out',
            '409': 'Conflict',
            '410': 'Gone',
            '411': 'Length Required',
            '412': 'Precondition Failed',
            '413': 'Request Entity Too Large',
            '414': 'Request-URL Too Large',
            '415': 'Unsupported Media Type',
            '416': 'Requested range not satisfiable',
            '417': 'Expectation Failed',
            '500': 'Internal Server Error',
            '501': 'Not Implemented',
            '502': 'Bad Gateway',
            '503': 'Service Unavailable',
            '504': 'Gateway Time-out',
            '505': 'HTTP Version not supported'
        }
        statusCode = JsonResponses.get(code, "Unknown HTTP Status Code")
        message = statusCode if not message else message
        return JsonResponse({
            "code": code,
            "data": message
        }, json_dumps_params={"separators": (',', ':')})


QJR = QuickJsonResponse_()
