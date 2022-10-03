import menu
import show_pupil_list_1
import add_pupil_2
import show_pupil_scores_3
import add_pupil_scores_4
import performance_5
import export_perf_6
import exit_7


def choose_action():
    run = True
    while run is True:
        action = menu.select_menu()

        if action == 1:
            show_pupil_list_1.show_p()

        if action == 2:
            add_pupil_2.add_p()

        if action == 3:
            show_pupil_scores_3.show_s()

        if action == 4:
            add_pupil_scores_4.add_s()

        if action == 5:
            performance_5.average_performance()

        if action == 6:
            export_perf_6.export_p()

        if action == 7:
            exit_7.exit_school()
            run = False


choose_action()
