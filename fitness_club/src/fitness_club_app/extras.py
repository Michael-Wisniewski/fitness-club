class Section(object):
    section = ''

    def get_context_data(self):
        context = super(Section, self).get_context_data()
        context['section'] = self.section
        return context