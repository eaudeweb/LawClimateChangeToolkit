def generate_code(model, instance):
    code = None
    if instance.parent:
        codes = [ob.code for ob in instance.parent.children.all() if ob]
        # if parent classification has children the increment
        # the last childen's code
        if codes:
            codes.sort(key=lambda x: [int(y) for y in x.split('.')])
            parts = codes[-1].split('.')
            parent_code = '.'.join(parts[:-1])
            last_code = parts[-1]
            code = '{0}.{1}'.format(parent_code, int(last_code) + 1)
        else:
            code = '{0}.1'.format(instance.parent.code)
    else:
        codes = [ob.code for ob in model.objects.filter(parent=None).all()]
        # if empty classification table - reinitialize code values
        if len(codes) == 0:
            codes = ['0']

        codes.sort(key=lambda x: [int(y) for y in x.split('.')])
        last_code = codes[-1]
        code = '{0}'.format(int(last_code) + 1)

    return code
