from .http import HtmxHttpRequest


def base_template(request: HtmxHttpRequest) -> dict[str, str]:
    if request.htmx:
        return {'base_template': 'core/html/_partial.html'}
    else:
        return {'base_template': 'core/html/_base.html'}
