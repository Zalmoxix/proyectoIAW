from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic


from .models import Incidencia


class IndexView(generic.ListView):
    template_name = 'registro/index.html'
    context_object_name = 'ultimas_incidencias'

    def get_queryset(self):
        return Incidencia.objects.order_by('-incidencia_fecha')[:5]


class DetailView(generic.DetailView):
    model = Incidencia
    template_name = 'registro/detail.html'


class ResultsView(generic.DetailView):
    model = Incidencia
    template_name = 'registro/results.html'

#def vote(request, question_id):
#    p = get_object_or_404(Question, pk=question_id)
#   try:
#        selected_choice = p.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the question voting form.
#        return render(request, 'polls/detail.html', {
#            'question': p,
#            'error_message': "You didn't select a choice.",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # Always return an HttpResponseRedirect after successfully dealing
#        # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
#        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
