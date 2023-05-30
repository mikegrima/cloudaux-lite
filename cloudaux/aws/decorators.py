"""
.. module: cloudaux.aws.decorators
    :platform: Unix
    :copyright: (c) 2018 by Netflix Inc., see AUTHORS for more
    :copyright: (c) 2023 by Mike Grima
    :license: Apache, see LICENSE for more details.
.. moduleauthor:: Patrick Kelley <pkelley@netflix.com> @monkeysecurity
.. moduleauthor:: Mike Grima <mike.r.grima@gmail.com>
"""
import functools


def paginated(response_key, request_pagination_marker="Marker", response_pagination_marker="Marker"):
    def decorator(func):
        @functools.wraps(func)
        def decorated_function(*args, **kwargs):
            results = []

            while True:
                response = func(*args, **kwargs)
                results.extend(response[response_key])

                # If the "next" pagination marker is in the response, then paginate. Responses may not always have
                # items in the response_key, so we should only key off of the response_pagination_marker.
                if response.get(response_pagination_marker):
                    kwargs.update({request_pagination_marker: response[response_pagination_marker]})
                else:
                    break
            return results
        return decorated_function
    return decorator
