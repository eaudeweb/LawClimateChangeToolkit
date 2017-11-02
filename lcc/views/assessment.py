from django.contrib.auth import mixins
from django.views.generic import TemplateView


class LegalAssessment(mixins.LoginRequiredMixin, TemplateView):
    template_name = "assessment.html"


class LegalAssessmentResults(mixins.LoginRequiredMixin, TemplateView):
    template_name = "assessment_results.html"
