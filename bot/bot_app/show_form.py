
def show_created_check_info(name: str, surname: str = None, patronymic: str = None, birthday: str = None, email: str = None,
                education: str = None, other_education: str = None, communities: str = None, practice_date: str = None, online_work: str = None,
                supervised: str = None, other_interests: str = None, kinolog_site: str = None, motivation: str = None, work_stages: str = None,
                dog_teaching: str = None, influenced_by: str = None, punishment: str = None, punishment_effect: str = None, ammunition: str = None,
                other_activities: str = None, work_methods: str = None, choice_importance: str = None, training_situation: str = None, advise: str = None, problem: str = None):
    text = "Анкета заполнена с следующими данными:\n"
    if not surname:
        text += f"Имя: {name}"
    elif not patronymic:
        text += f"Имя: {name}\nФамилия: {surname}"
    elif not birthday:
        text += f"1. ФИО: {surname} {name} {patronymic}"
    elif not email:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}"
    elif not education:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}"
    elif not other_education:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}"
    elif not communities:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
    elif not practice_date:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}"
    elif not online_work:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}"
    elif not supervised:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}"
    elif not other_interests:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}"
    elif not kinolog_site:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
    elif not motivation:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}"
    elif not work_stages:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}"
    elif not dog_teaching:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}"
    elif not influenced_by:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}"
    elif not punishment:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}\n15. Источник вдохновения в плане работы с собаками: {influenced_by}\n"
    elif not punishment_effect:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}\n15. Источник вдохновения в плане работы с собаками: {influenced_by}\n"
        text += f"16. Мнение о наказании собак: {punishment}"
    elif not ammunition:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}\n15. Источник вдохновения в плане работы с собаками: {influenced_by}\n"
        text += f"16. Мнение о наказании собак: {punishment}\n17. Влияния наказаний: {punishment_effect}"
    elif not other_activities:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}\n15. Источник вдохновения в плане работы с собаками: {influenced_by}\n"
        text += f"16. Мнение о наказании собак: {punishment}\n17. Влияния наказаний: {punishment_effect}\n18. Использованные амуниции: {ammunition}"
    elif not work_methods:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}\n15. Источник вдохновения в плане работы с собаками: {influenced_by}\n"
        text += f"16. Мнение о наказании собак: {punishment}\n17. Влияния наказаний: {punishment_effect}\n18. Использованные амуниции: {ammunition}\n19. Игры или занятия: {other_activities}"
    elif not choice_importance:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}\n15. Источник вдохновения в плане работы с собаками: {influenced_by}\n"
        text += f"16. Мнение о наказании собак: {punishment}\n17. Влияния наказаний: {punishment_effect}\n18. Использованные амуниции: {ammunition}\n19. Игры или занятия: {other_activities}\n20. Методики: {work_methods}"
    elif not training_situation:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}\n15. Источник вдохновения в плане работы с собаками: {influenced_by}\n"
        text += f"16. Мнение о наказании собак: {punishment}\n17. Влияния наказаний: {punishment_effect}\n18. Использованные амуниции: {ammunition}\n19. Игры или занятия: {other_activities}\n20. Методики: {work_methods}\n21. Важность выбора: {choice_importance}"
    elif not advise:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}\n15. Источник вдохновения в плане работы с собаками: {influenced_by}\n"
        text += f"16. Мнение о наказании собак: {punishment}\n17. Влияния наказаний: {punishment_effect}\n18. Использованные амуниции: {ammunition}\n19. Игры или занятия: {other_activities}\n20. Методики: {work_methods}\n21. Важность выбора: {choice_importance}\n22. Ситуация с дрессировкой собаки: {training_situation}"
    elif not problem:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}\n15. Источник вдохновения в плане работы с собаками: {influenced_by}\n"
        text += f"16. Мнение о наказании собак: {punishment}\n17. Влияния наказаний: {punishment_effect}\n18. Использованные амуниции: {ammunition}\n19. Игры или занятия: {other_activities}\n20. Методики: {work_methods}\n21. Важность выбора: {choice_importance}\n22. Ситуация с дрессировкой собаки: {training_situation}\n23. Совет владельцам собак: {advise}"
    else:
        text += f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
        text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
        text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}\n15. Источник вдохновения в плане работы с собаками: {influenced_by}\n"
        text += f"16. Мнение о наказании собак: {punishment}\n17. Влияния наказаний: {punishment_effect}\n18. Использованные амуниции: {ammunition}\n19. Игры или занятия: {other_activities}\n20. Методики: {work_methods}\n21. Важность выбора: {choice_importance}\n22. Ситуация с дрессировкой собаки: {training_situation}\n23. Совет владельцам собак: {advise}\n24. Предпочтительная для решения проблема собак: {problem}"

    return text


def show_kinolog_info(name: str, surname: str = None, patronymic: str = None, birthday: str = None, email: str = None,
                education: str = None, other_education: str = None, communities: str = None, practice_date: str = None, online_work: str = None,
                supervised: str = None, other_interests: str = None, kinolog_site: str = None, motivation: str = None, work_stages: str = None,
                dog_teaching: str = None, influenced_by: str = None, punishment: str = None, punishment_effect: str = None, ammunition: str = None,
                other_activities: str = None, work_methods: str = None, choice_importance: str = None, training_situation: str = None, advise: str = None, problem: str = None):
    text = f"1. ФИО: {surname} {name} {patronymic}\n2. День рождения: {birthday}\n3. Почта: {email}\n4. Высшее образование: {education}\n5. Курсы или дополнительное образование: {other_education}"
    text += f"\n6. Профессиональные сообщества, ассоциация: {communities}\n7.Кинологическая практика: {practice_date}\n8. Опыт работы онлайн: {online_work}\n9. Супервизия: {supervised}\n10. Другая работа кроме специалиста по поведению собак: {other_interests}\n"
    text += f"11. Персональный сайт с услугами: {kinolog_site}\n12. Источник мотивации к работе с собаками и людьми: {motivation}\n13. Этапы работы с клиентом: {work_stages}\n14. Собаку важно научить: {dog_teaching}\n15. Источник вдохновения в плане работы с собаками: {influenced_by}\n"
    text += f"16. Мнение о наказании собак: {punishment}\n17. Влияния наказаний: {punishment_effect}\n18. Использованные амуниции: {ammunition}\n19. Игры или занятия: {other_activities}\n20. Методики: {work_methods}\n21. Важность выбора: {choice_importance}\n22. Ситуация с дрессировкой собаки: {training_situation}\n23. Совет владельцам собак: {advise}\n24. Предпочтительная для решения проблема собак: {problem}"
    return text