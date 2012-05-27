from django import template
register = template.Library()


@register.inclusion_tag('score.html')
def render_score(endorsement):
    score = endorsement.score
    if score > 0:
        img_name = 'up.png'
        klass = 'up'
    elif score < 0:
        img_name = 'down.png'
        klass = 'down'
    else:
        img_name = 'neutral.png'
        klass = 'neutral'
    return dict(img_name=img_name, klass=klass)
    
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
    
@register.inclusion_tag('endorser_popover.html')
def render_endorser_popover(endorser):
    return dict(endorser=endorser)
    

    

    

    

    
