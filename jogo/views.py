# jogo/views.py
from django.shortcuts import render, redirect
from .models import Phase
from django.views.decorators.csrf import csrf_exempt
from .models import Phase
import json
from django.http import JsonResponse

def index(request):
    """View para a página inicial com instruções"""
    return render(request, 'game/index.html')

def phase(request, phase_number):
    """View para exibir cada fase do jogo"""
    try:
        # Tenta encontrar a fase pelo número
        current_phase = Phase.objects.get(number=phase_number)
    except Phase.DoesNotExist:
        # Se não existir, redireciona para a página inicial
        return redirect('index')
    
    return render(request, 'game/phase.html', {
        'phase': current_phase
    })

def check_answer(request):
    if request.method == 'POST':
        try:
            # Carrega os dados do corpo da requisição
            data = json.loads(request.body)
            phase_number = data.get('phase_number')
            click_x = data.get('click_x')
            click_y = data.get('click_y')

            # Validação básica dos dados
            if None in [phase_number, click_x, click_y]:
                return JsonResponse({'error': 'Dados incompletos'}, status=400)

            # Conversão para inteiros
            phase_number = int(phase_number)
            click_x = int(click_x)
            click_y = int(click_y)

            # Busca a fase
            phase = Phase.objects.get(number=phase_number)

            # Verifica as coordenadas
            if (abs(click_x - phase.object_x) <= phase.tolerance and 
                abs(click_y - phase.object_y) <= phase.tolerance):
                
                # Resposta de sucesso
                return JsonResponse({
                    'success': True,
                    'redirect_url': f'/phase/{phase_number + 1}/' if phase_number < 12 else '/congratulations/'
                })
                
            return JsonResponse({'success': False})

        except Phase.DoesNotExist:
            return JsonResponse({'error': 'Fase não encontrada'}, status=404)
        except ValueError:
            return JsonResponse({'error': 'Valores inválidos'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método não permitido'}, status=405)

def congratulations(request):
    """View para a tela final de parabéns"""
    return render(request, 'game/congratulations.html')