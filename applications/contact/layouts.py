from crispy_forms.layout import HTML


def contact_us_layout(fields):
    fields.append("name")
    fields.append("email")
    fields.append("message")
    fields.append("captcha")

    fields.append(HTML(
        """
        <hr>
        <div class="text-right">
            <button class="btn btn-primary" type="submit">
                Enviar
            </button>
        </div>
        """
    ))

    return fields

