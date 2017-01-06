#-*- coding: utf-8 -*-

from Tkinter import *
import ttk
import io
# import tkHyperlinkManager
import webbrowser
import common_modules as cm

""" For GUI to work it requires specific local filesystem """

""" PRE GUI DATA PREPARATION """


def ready_main_list(main_list):
    print "MAKING MAIN_LIST ADJUSTMENT ACCORDING TO LOADING CRITEREAS...."
    """ ready_main_list:
        - homepage first others sorted according to text file length,
        - number of list items limited to 20 """
    sorted_main_list = [] 

    for ind in range(len(main_list)):        
        main_list[ind].insert(0, main_list[ind][4]) # Making text length criteria first in a row for sorting of the rows
        main_list[ind].pop(5)


    sorted_main_list.append(main_list[0])
    main_list.pop(0)
    part_of_sorted = sorted(main_list, reverse=True)
    sorted_main_list = sorted_main_list + part_of_sorted
    ready_main_list = sorted_main_list[0:20]
    print "LENGTH OF READY MAIN_LIST:", len(ready_main_list)

    return ready_main_list

def find_highlight_position(text_as_list, hi_keyword):
    h_position_list = []
    for ind in range(len(text_as_list)):
        h_position_entry = []
        track_s_line = ind
        track_s_symbol = text_as_list[ind].find(hi_keyword)

        if track_s_symbol > (-1):
            h_position_entry.append(track_s_line)
            h_position_entry.append(track_s_symbol)
            h_position_list.append(h_position_entry)
        else:
            pass
    return h_position_list

""" GUI CLASS """

class Veri_GUI(object):
    def __init__(self, root):

        self.root = root
        root.title("VERI")
        self.cont = ttk.Frame(root, relief='sunken')
        # Additional styling for notebook and tabs
        self.change_noteb = ttk.Style()
        self.change_tab = ttk.Style()
        self.change_noteb.configure('TNotebook', tabposition='wn')
        self.change_tab.configure('TNotebook.Tab', borderwidth=5)
        #/
        self.noteb = ttk.Notebook(self.cont)
        self.button_frame = ttk.Frame(self.cont, relief='sunken')
        self.good_button = Button(self.button_frame, text='VERI_GOOD', width=20, height=5, bg='green', command=self.veri_good_b)
        self.bad_button = Button(self.button_frame, text='VERI_BAD', width=20, height=5, bg='red', command=self.veri_bad_b)
        self.h_light_frame = Frame(self.cont, relief='raised', background='yellow', borderwidth='3')
        

        # Text box for highlight input
        self.input_header = ttk.Label(self.h_light_frame, text='TEST_key', background='yellow')
        self.input_as_text = Text(self.h_light_frame, width=20, height=39, borderwidth=3, relief='sunken')
        #/

        # griding of static gui components
        self.cont.grid(column=0, row=0, sticky=(N,W,S,E))
        self.button_frame.grid(column=0, row=0, sticky=(N,W,S,E))
        self.noteb.grid(column=0, row=1, sticky=(N,W,S,E))
        self.good_button.grid(column=0, row=0, sticky=(N,W))
        self.bad_button.grid(column=1, row=0, sticky=(N,W))
        self.h_light_frame.grid(column=1, row=0, rowspan=2, padx=3)
        self.input_header.grid(column=0, row=0, sticky=(N,S))
        self.input_as_text.grid(column=0, row=1, sticky=(N,S))
        #/
        # max no. == 20 of tabs instantiated
        self.t_tab0 = Text(self.noteb, width=100, height=40, font=("Arial", "10"))                                                                                                                        
        self.t_tab1 = Text(self.noteb)
        self.t_tab2 = Text(self.noteb)
        self.t_tab3 = Text(self.noteb)
        self.t_tab4 = Text(self.noteb)
        self.t_tab5 = Text(self.noteb)
        self.t_tab6 = Text(self.noteb)
        self.t_tab7 = Text(self.noteb)
        self.t_tab8 = Text(self.noteb)
        self.t_tab9 = Text(self.noteb)
        self.t_tab10 = Text(self.noteb)
        self.t_tab11 = Text(self.noteb)
        self.t_tab12 = Text(self.noteb)
        self.t_tab13 = Text(self.noteb)
        self.t_tab14 = Text(self.noteb)
        self.t_tab15 = Text(self.noteb)
        self.t_tab16 = Text(self.noteb)
        self.t_tab17 = Text(self.noteb)
        self.t_tab18 = Text(self.noteb)
        self.t_tab19 = Text(self.noteb)

        self.t_tab_list = [self.t_tab0, self.t_tab1, self.t_tab2, self.t_tab3, self.t_tab4, self.t_tab5,
                            self.t_tab6, self.t_tab7, self.t_tab8, self.t_tab9, self.t_tab10, self.t_tab11,
                            self.t_tab12, self.t_tab13, self.t_tab14, self.t_tab15, self.t_tab16, self.t_tab17,
                            self.t_tab18, self.t_tab19]

        self.very_ready_f_name = '1_ready_for_veri.txt'
        self.very_good_f_name = '2_1_good_veri.txt'
        self.very_bad_f_name = '2_2_bad_veri.txt'
        self.no_domain = ''
        self.key_list_name = '3_p_name_highlights.txt'
        """ !!! Don't forget to set it to zero when loading a new page """
        self.site_text_as_list = []

        self.veri_ready_list = cm.l_of_l_read(self.no_domain, self.very_ready_f_name)

        # HIGHLIGHTS FUCTIONALITY
        # .Initial tab text highlighting of keywords from txt file Done
        # ..Retrieving keywords from txt and converting to active list Done
        self.init_h_key_list = cm.l_of_l_read(self.no_domain, self.key_list_name)
        if len(self.init_h_key_list) > 0:
            self.test_hi_key_list = self.init_h_key_list[0]
            # .Init h_keywords in text box
            self.key_as_text = '\n'.join(self.test_hi_key_list) + '\n'
            self.input_as_text.insert(END, self.key_as_text)
        else:
            self.test_hi_key_list = []
            print "The initial highlight key list is empty"

        print "HIGHLIGHT LIST................\n", self.init_h_key_list
        self.input_as_text.bind('<Return>', self.key_h_light)
        #/

        # Initial tab data loading
        self.init_url_data = self.veri_ready_list[0]
        # self.veri_ready_list.pop(0) # removing intial entry from input_list

        self.init_tab_data_set = self.tabs_data_set(self.init_url_data)
        self.laod_tabs(self.init_tab_data_set)
        #/



    def tabs_data_set(self, url_data):
        "PREPARING MAIN_LIST FOR LOADING................"
        base_url = url_data[3]
        url_domain = cm.strip_to_domain(base_url) # domain acts as key in filesystem composed of folders named as domains
        print "DOMAIN LOADING: ", url_domain
        main_list_f_name = 'main_list.txt'
        main_list = cm.l_of_l_read(url_domain, main_list_f_name)
        print "MAIN_LIST RETRIEVED:\n "
        # for item in main_list:
            # print item
        url_r_main_list = ready_main_list(main_list)
        # print "MAIN_LIST AFTER ADJUSTMENTS(READY):\n", url_r_main_list
        # for item in url_r_main_list:
            # print item
        return url_r_main_list

    def laod_tabs(self, url_ready_main_list):
        "LOADING TABS..................."
        for ind in range(len(url_ready_main_list)):
            # Variables used
            base_url = url_ready_main_list[0][2]
            url_domain = cm.strip_to_domain(base_url)
            active_tab_title =  url_ready_main_list[ind][3]
            link_url = url_ready_main_list[ind][2]
            active_link_url_no_domain = link_url.replace(base_url,'...')
            active_tab = self.t_tab_list[ind]
            page_text_f_name = url_ready_main_list[ind][4]
            #/

            self.noteb.add(active_tab, text='%s\n%s' % (active_tab_title, active_link_url_no_domain))

            for_hyper = link_url + '\n\n'
            active_tab.insert(END, for_hyper)

            page_text_as_list = cm.text_retrieve(url_domain, page_text_f_name)

            page_text = ''.join(page_text_as_list)

            # print "RETRIVED TEXT FOR TAB IN ...................\n %r" % page_text
            active_tab.insert(END, page_text) # Adding retrieved text to notebook text window
            

            active_tab.tag_add('hyper', '1.0', '1.%d' % len(for_hyper))
            active_tab.tag_config('hyper', foreground='blue')
            active_tab.tag_bind('hyper', "<Enter>", lambda event, arg=ind: self.mouse_on(event, arg))
            active_tab.tag_bind('hyper', "<Leave>", lambda event, arg=ind: self.mouse_of(event, arg))
            active_tab.tag_bind('hyper', "<Button-1>", lambda event, arg=link_url: self.hyper(event, arg))

            #collecting highlighting positions according to keyword in tab text Done
            
            for test_key in self.test_hi_key_list:
                self.h_key_highlight(test_key, active_tab, page_text_as_list)

            # collecting site text as list for highlighting functionality

            self.site_text_as_list.append(page_text_as_list)

            page_key_word = ["Om-oss", "om-oss", "om oss", "OM-OSS"]
            if (page_key_word[0] or page_key_word[1] or page_key_word[2] or page_key_word[3]) in link_url:
                self.noteb.select(active_tab)

    def h_key_highlight(self, new_key, active_tab, page_text_as_list):
        tab_key_p_list = find_highlight_position(page_text_as_list, new_key)
        print "HIGHLIGHT POSITIONS FOUND for new_key %r:\n" % new_key, tab_key_p_list

        # highlighting new_key in tab text Done
        for s_line_s_symbol in tab_key_p_list:
            # print "s_line_s_symbol:", s_line_s_symbol
            s_line = s_line_s_symbol[0] + 3 # offseting lines to compensate for added hyperlink at the beginning of the tab text
            s_symbol = s_line_s_symbol[1]
            e_line = s_line
            e_symbols = s_symbol + len(new_key)
            str_s_line = str(s_line)
            str_s_symbol = str(s_symbol)
            str_e_line = str(e_line)
            str_e_symbols = str(e_symbols)
            active_tab.tag_add('highlight%s.%s' % (str_s_line, str_s_symbol), '%s.%s' % (str_s_line, str_s_symbol), '%s.%s' % (str_e_line, str_e_symbols))
            active_tab.tag_config('highlight%s.%s' % (str_s_line, str_s_symbol), background='yellow')

    def h_key_high_remove(self):
        pass


    def delete_tabs(self, old_tab_data_set):
        for ind in range(len(old_tab_data_set)):
            self.t_tab_list[ind].delete('1.0', END)
            self.noteb.forget(self.t_tab_list[ind])

    def mouse_on(self, event, ind):
            self.t_tab_list[ind].config(cursor="hand2")

    def mouse_of(self, event, ind):
            self.t_tab_list[ind].config(cursor="")

    def hyper(self, event, link_url):
        webbrowser.open_new(link_url)
            
    def veri_good_b(self):

        old_tab_data_set = self.init_tab_data_set
        print "TABS LIST LENGTH FOR DELETING:", len(old_tab_data_set)
        self.delete_tabs(old_tab_data_set)
        current_link_entry = self.veri_ready_list[0] # link entry showing in GUI same as init value

        self.veri_ready_list = cm.l_of_l_read(self.no_domain, self.very_ready_f_name)
        next_link_entry = self.veri_ready_list[1]

        self.init_tab_data_set = self.tabs_data_set(next_link_entry)
        current_tab_data_set = self.init_tab_data_set
        self.laod_tabs(current_tab_data_set)

        self.veri_ready_list.pop(0)
        cm.l_of_l_write(self.no_domain, self.veri_ready_list, self.very_ready_f_name)


        cm.txt_file_append(self.no_domain, current_link_entry, self.very_good_f_name)
        self.site_text_as_list = [] # Clearing site text list

    def veri_bad_b(self):
        pass

        old_tab_data_set = self.init_tab_data_set
        print "TABS LIST LENGTH FOR DELETING:", len(old_tab_data_set)
        self.delete_tabs(old_tab_data_set)
        current_link_entry = self.veri_ready_list[0] # link entry showing in GUI same as init value

        self.veri_ready_list = cm.l_of_l_read(self.no_domain, self.very_ready_f_name)
        next_link_entry = self.veri_ready_list[1]

        self.init_tab_data_set = self.tabs_data_set(next_link_entry)
        current_tab_data_set = self.init_tab_data_set
        self.laod_tabs(current_tab_data_set)

        self.veri_ready_list.pop(0)
        cm.l_of_l_write(self.no_domain, self.veri_ready_list, self.very_ready_f_name)


        cm.txt_file_append(self.no_domain, current_link_entry, self.very_bad_f_name)
        self.site_text_as_list = [] # Clearing site text list

    def key_h_light(self, event):
        dif_type_key_list = []
        # Text retrieve Done     
        test_input = self.input_as_text.get('1.0', END)
        # Convert text to list Done
        test_key_input_list = test_input.split('\n')
        if len(test_key_input_list[-1]) < 1: # in cases where txt file has newline in last empty line pops last item
            test_key_input_list.pop(-1)
        print "Key test_input list: %s" % test_key_input_list
        dif_type_key_list.append(test_key_input_list)
        # Highlight entered key in the tab text
        # Compare init list with the list after action
        if len(test_key_input_list) > len(self.test_hi_key_list): # new h_key added to text box
            for ind in range(len(self.init_tab_data_set)):
                active_tab = self.t_tab_list[ind]
                new_key = test_key_input_list[-1]
                active_page_text_as_list = self.site_text_as_list[ind]
                self.h_key_highlight(new_key, active_tab, active_page_text_as_list)

            # .Write new key list to txt file
            cm.l_of_l_write(self.no_domain, dif_type_key_list, self.key_list_name)
        elif len(test_key_input_list) == len(self.test_hi_key_list): # enter presed without new adding anything
            return 'break'
        else:
            # .Write new key list to txt file
            cm.l_of_l_write(self.no_domain, dif_type_key_list, self.key_list_name)
        # 
        print "convert to test_key_input_list WORKS !!!\n%r" % test_key_input_list
    

root = Tk()
gui_object = Veri_GUI(root)

root.mainloop()


