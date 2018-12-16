class Section():
    section = ''

    def get_context_data(self, **kwargs):
        context = super(Section, self).get_context_data(**kwargs)
        context['section'] = self.section
        return context