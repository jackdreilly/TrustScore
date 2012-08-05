class AutoPrintMixin(object):
    
    def to_string(self):
        return super(AutoPrint, self.__repr__())
        
    def __repr__(self):
        return self.to_string()
    def __str__(self):
        return self.to_string()
    def __unicode__(self):
        return self.to_string()