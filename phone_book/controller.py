import menu
import contact_view
import contact_add
import export_pb
import import_pb
import exit_pb


def choose_action():
    run = True
    while run is True:
        action = menu.select_menu()

        if action == 1:
            contact_view.contact_search_by_surname()

        if action == 2:
            contact_add.add_new_contact()

        if action == 3:
            export_pb.export_contacts()

        if action == 4:
            import_pb.import_contacts()

        if action == 5:
            exit_pb.exit_phone_book()
            run = False


choose_action()
