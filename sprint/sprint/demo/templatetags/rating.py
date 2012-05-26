from django import template
register = template.Library()


@register.inclusion_tag('score.html')
def render_score(endorsement):
    score = endorsement.score
    if score > 0:
        img_name = 'up.png'
    elif score < 0:
        img_name = 'down.png'
    else:
        img_name = 'neutral.png'
    return dict(img_name=img_name)
    
@register.inclusion_tag('endorsements.html')
def render_endorsements(endorsements):
    return dict(endorsements=endorsements)
    
@register.inclusion_tag('endorsement.html')
def render_endorsement(endorsement):
    return dict(endorsement=endorsement)
    
@register.inclusion_tag('agent_info.html')
def render_agent_info(agent):
    return dict(agent=agent)
    
@register.inclusion_tag('loans.html')
def render_loans(loans):
    return dict(loans=loans)
    
@register.inclusion_tag('loan.html')
def render_loan(loan):
    return dict(loan=loan)
    

    

    

    
