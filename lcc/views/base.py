from collections import defaultdict
from lcc import models


class UserPatchMixin():
    def dispatch(self, request, *args, **kwargs):
        self.user_profile = None
        if request.user.is_authenticated:
            self.user_profile = models.UserProfile.objects.get(
                user=request.user
            )
            request.user_profile = self.user_profile
        return super(UserPatchMixin, self).dispatch(request, *args, **kwargs)


class TagGroupRender():
    def __init__(self, tag_group):
        self.name = tag_group.name
        self.pk = tag_group.pk
        self.tags = [{'name': tag.name, 'pk': tag.pk}
                     for tag in models.TaxonomyTag.objects.filter(
                group=tag_group)]


class TaxonomyFormMixin:
    def get_form_kwargs(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }

        if self.request.method in ('POST', 'PUT'):
            post_data = self.request.POST
            kwargs['data'] = defaultdict(list)
            for field in post_data.keys():
                if "classification" in field:
                    kwargs['data']["classifications"].append(int(field.split("_")[1]))
                elif "tag" in field:
                    kwargs['data']['tags'].append(int(field.split("_")[1]))
                else:
                    kwargs['data'][field] = post_data[field]
            kwargs['files'] = self.request.FILES
            for file in kwargs['files'].keys():
                kwargs['data'][file + "_name"] = kwargs['files'][file].name

        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
        return kwargs


def taxonomy_to_string(legislation, tags=False, classification=False):
    if tags:
        return ", ".join(list(legislation.tags.values_list('name', flat=True)))

    if classification:
        return ", ".join(
            list(legislation.classifications.values_list('name', flat=True))
        )
