from django import template
register = template.Library()


@register.inclusion_tag('score.html')
def render_score(endorsement):
    """
    render books for user
    in turn calls the render_person method for members
    """
    score = endorsement.score
    if score > 0:
        img_name = 'up.png'
    elif score < 0:
        img_name = 'down.png'
    else:
        img_name = 'neutral.png'
    return dict(img_name=img_name)