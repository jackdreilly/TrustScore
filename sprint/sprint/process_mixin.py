class ProcessAfterSaveMixin(object):

    def process(self):
        pass

    def save(self, do_process = True, *args, **kwargs):
        super(ProcessAfterSaveMixin, self).save(*args, **kwargs)
        if do_process:
            self.process()