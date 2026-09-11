import nh3

def sanitize_html(html):
    return nh3.clean(
        html,
        tags={
            "a",
            "img",
            "audio",
            "strong",
            "em",
            "h1",
            "h2",
            "h3",
            "li",
            "ol",
            "ul",
            "p",
            "br",
            "u",
            "iframe",
        },
        attributes={
            "a": {"href"},
            "img": {"src", "width", "height"},
            "audio": {"src", "controls", "preload"},
            "iframe": {"src"},
        },
    )