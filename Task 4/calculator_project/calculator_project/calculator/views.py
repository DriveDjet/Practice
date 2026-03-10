from django.shortcuts import render
from django.http import JsonResponse
import json

def index(request):
    """Главная страница с калькулятором"""
    return render(request, 'calculator/index.html')

def calculate(request):
    """API для вычислений"""
    if request.method == 'POST':
        try:
            # Получаем данные из POST-запроса
            data = json.loads(request.body)
            num1 = data.get('num1')
            num2 = data.get('num2')
            operation = data.get('operation')

            # Проверяем наличие всех данных
            if num1 is None or num2 is None or operation is None:
                return JsonResponse({
                    'success': False,
                    'error': 'Отсутствуют необходимые данные'
                })

            # Пробуем преобразовать в числа
            try:
                num1 = float(num1)
                num2 = float(num2)
            except (TypeError, ValueError):
                return JsonResponse({
                    'success': False,
                    'error': 'Пожалуйста, введите корректные числа'
                })

            # Выполняем операцию
            result = None
            if operation == 'sum':
                result = num1 + num2
            elif operation == 'difference':
                result = num1 - num2
            elif operation == 'product':
                result = num1 * num2
            elif operation == 'division':
                if num2 == 0:
                    return JsonResponse({
                        'success': False,
                        'error': 'Деление на ноль невозможно'
                    })
                result = num1 / num2
            else:
                return JsonResponse({
                    'success': False,
                    'error': 'Неизвестная операция'
                })

            # Округляем результат до 10 знаков после запятой для красоты
            if isinstance(result, float):
                result = round(result, 10)
                # Убираем .0 если число целое
                if result.is_integer():
                    result = int(result)

            return JsonResponse({
                'success': True,
                'result': result
            })

        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Ошибка в формате данных'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Произошла ошибка: {str(e)}'
            })

    return JsonResponse({
        'success': False,
        'error': 'Метод не поддерживается'
    })