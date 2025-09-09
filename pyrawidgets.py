import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import pyra
from datetime import datetime, date, time, timedelta

class LinearDateSelector():
    '''วิตเจ็ตกลุ่มที่ใช้เลือกวันที่ด้วยปุ่มไปข้างหน้า ย้อนกลับ และไปยังวันที่ปัจจุบัน\n
    สามารถตั้งค่าช่วงวันที่ วันในสัปดาห์ที่ต้องการข้าม และวันหยุดที่ต้องการข้ามได้'''
    def __init__(self, master, stylename_caption="TLabel", stylename_button="TButton", indefinite_range=True, dates_to_omit=('Sun'), holidays_to_omit=(date(year=2024,month=12,day=31),date(year=2025,month=1,day=1))):
        self.datevar = date.today()
        self.strvar_date = tk.StringVar(value=pyra.ReformatDate(date_to_reformat=self.datevar, format_type='long', locale='TH',yearsystem='BE'))
        self.strvar_dayofweek = tk.StringVar(value=pyra.getWeekday(d=self.datevar, format_type='full', locale='TH'))
        self.indefinite_range=indefinite_range
        self.dates_to_omit=dates_to_omit
        self.holidays_to_omit=holidays_to_omit
        self.stylename_caption = stylename_caption if stylename_caption is not None else "TLabel"
        self.stylename_button = stylename_button if stylename_button is not None else "TButton"

        self.dayofweek = tk.StringVar()
        self.widgetframe = ttk.Frame(master=master)
        self.button_prevdate = ttk.Button(master=self.widgetframe, text='◀', command=lambda:self.changeDate(direction=-1), style=self.stylename_button)
        self.button_jumptotoday = ttk.Button(master=self.widgetframe, text='TODAY', command=self.jumptoToday, style=self.stylename_button)
        self.button_nextdate = ttk.Button(master=self.widgetframe, text='▶', command=lambda:self.changeDate(direction=1), style=self.stylename_button)
        self.subframe_date = ttk.Frame(master=self.widgetframe)
        self.textlabel_date = ttk.Label(master=self.subframe_date, textvariable=self.strvar_date, style=self.stylename_caption)
        self.textlabel_datecaption = ttk.Label(master=self.subframe_date, textvariable=self.strvar_dayofweek, style=self.stylename_caption)

    def pwpack(self, side, padx=0, pady=0):
        self.widgetframe.pack(side=side, fill='x', padx=padx, pady=pady,expand=1)
        self.button_prevdate.pack(side='left',anchor='w', padx=5, pady=5)
        self.button_jumptotoday.pack(side='left',anchor='e', padx=5, pady=5)
        self.button_nextdate.pack(side='left',anchor='e', padx=5, pady=5)
        self.subframe_date.pack(side='left', padx=5, pady=5, fill='both', expand=1)
        self.textlabel_date.pack(side='top', fill='x')
        self.textlabel_datecaption.pack(side='top', fill='x')
        

    def changeDate(self, direction):
        change = timedelta(days=float(direction))
        
        newdate = self.datevar.__add__(change)
        self.strvar_date.set(pyra.ReformatDate(date_to_reformat=newdate, format_type='long', locale='TH',yearsystem='BE'))
        self.strvar_dayofweek.set(pyra.getWeekday(d=newdate, format_type='full', locale='TH'))
        self.datevar = newdate

        if newdate in self.holidays_to_omit:
            self.changeDate(direction=direction)
        elif pyra.getWeekday(d=newdate, format_type='abbr', locale='EN') in self.dates_to_omit:
            self.changeDate(direction=direction)

    def jumptoToday(self):
        self.strvar_date.set(pyra.ReformatDate(date_to_reformat=date.today(), format_type='long', locale='TH',yearsystem='BE'))
        self.strvar_dayofweek.set(pyra.getWeekday(d=date.today(), format_type='full', locale='TH'))
        self.datevar = date.today()

    def jumptoDate(self,to_date:date|datetime):
        d = to_date.date() if type(to_date) is datetime else to_date
        self.strvar_date.set(pyra.ReformatDate(date_to_reformat=d, format_type='long', locale='TH',yearsystem='BE'))
        self.strvar_dayofweek.set(pyra.getWeekday(d=d, format_type='full', locale='TH'))
        self.datevar = d

    @property
    def next_button(self):
        '''เรียก property นี้เพื่อใช้ร่วมกับการ bind คำสั่งเพิ่มเติมเมื่อคลิกปุ่มไปข้างหน้า\nคำแนะนำ: ใช้ sequence เป็น <Button-1> เพื่อกำหนดเหตุการณ์การคลิกปุ่มเมาส์หลัก'''
        return self.button_nextdate
    
    @property
    def prev_button(self):
        '''เรียก property นี้เพื่อใช้ร่วมกับการ bind คำสั่งเพิ่มเติมเมื่อคลิกปุ่มย้อนกลับ\nคำแนะนำ: ใช้ sequence เป็น <Button-1> เพื่อกำหนดเหตุการณ์การคลิกปุ่มเมาส์หลัก'''
        return self.button_prevdate
    
    @property
    def today_button(self):
        '''เรียก property นี้เพื่อใช้ร่วมกับการ bind คำสั่งเพิ่มเติมเมื่อคลิกปุ่มไปยังวันนี้\nคำแนะนำ: ใช้ sequence เป็น <Button-1> เพื่อกำหนดเหตุการณ์การคลิกปุ่มเมาส์หลัก'''
        return self.button_jumptotoday

    @property
    def chosenDate(self):
        return self.datevar
    
    # @property
    # def selectedtimestamp(self):
    #     return pyra.CreateDataTimestamp()

'''
class TabularFrame():
    วิตเจ็ตกลุ่มที่ประกอบไปด้วยเฟรมหลักหนึ่งเฟรม และเฟรมย่อยสองเฟรมวางต่อกันในแนวตั้ง\n
    มีหัวตารางอยู่ด้านบน และเฟรมแถวพร้อมแถบเลื่อนแนวตั้งด้านล่าง
    def __init__(self, master):
        self.widgetframe = ttk.Frame(master=master)
        self.subframe_header = ttk.Frame(master=self.widgetframe)
        self.subframe_content = tk.Canvas(master=self.widgetframe)
        self.tabulate_yscroll = ttk.Scrollbar(master=self.subframe_content, orient='vertical', command=self.subframe_content.yview)
        self.tabulate_xscroll = ttk.Scrollbar(master=self.subframe_content, orient='horizontal', command=self.subframe_content.xview)
        self.subframe_content.configure(yscrollcommand=self.tabulate_yscroll.set, xscrollcommand=self.tabulate_xscroll.set)
        self.subframe_table = ttk.Frame(master=self.subframe_content)
        self.subframe_content.create_window((0,0), window=self.subframe_table, anchor='nw')
        self.subframe_table.bind("<Configure>", self.on_frame_configure)
        self.thing = SimpleCalendar(master=self.subframe_table)

    def pwpack(self, side, padx, pady):
        self.widgetframe.pack(side=side, padx=padx, pady=pady, fill='both', expand=1)
        self.subframe_header.pack(side='top', fill='x')
        self.subframe_content.pack(side='top', fill='both', expand=1)
        self.tabulate_yscroll.pack(side='right', fill='y')
        self.tabulate_xscroll.pack(side='bottom', fill='x')
        self.thing.pwpack(side='top')

    def on_frame_configure(self, event):
        self.subframe_content.configure(scrollregion=self.subframe_content.bbox("all"))

    def add_column(self, column_type):
        if column_type not in ('entry', 'check', 'dropdown', 'rowid', 'action_edit', 'action_delete', 'action_reset', 'action_move_up', 'action_move_down', 'action_move_totop', 'action_move_tobottom'):
            raise AttributeError("Invalid column_type tag.")
'''

class LinearMonthSelector():
    def __init__(self, master):
        self.stylename_caption ="H3ol.TLabel"
        self.stylename_button = "Outline.TButton"

        self.chosendate = date.today()
        self.datevar_month = date(date.today().year, date.today().month, 1)
        self.strvar_monthdate = tk.StringVar(value=str(pyra.ReformatDate(date_to_reformat=self.datevar_month,format_type='long',locale='TH', yearsystem='BE').split(sep=' ' ,maxsplit=1)[1]))
        self.widgetframe = ttk.Frame(master=master)

        self.subframe_monthselector = ttk.Frame(master=self.widgetframe)
        self.button_prevmonth = ttk.Button(master=self.subframe_monthselector, text='◀', style=self.stylename_button, command=lambda:self.changeMonth(-1))
        self.button_jumptotoday = ttk.Button(master=self.subframe_monthselector, text='TODAY', style=self.stylename_button, command=self.jumptoThisMonth)
        self.button_nextmonth = ttk.Button(master=self.subframe_monthselector, text='▶', style=self.stylename_button, command=lambda:self.changeMonth(1))
        self.subframe_month = ttk.Frame(master=self.subframe_monthselector)
        self.textlabel_currentmonth = ttk.Label(master=self.subframe_month, textvariable=self.strvar_monthdate, justify='center', style=self.stylename_caption)

    def pwpack(self, side, padx=0, pady=0):
        self.widgetframe.pack(side=side, fill='x', expand=0, padx=padx, pady=pady)
        self.subframe_monthselector.pack(side='top', padx=5, pady=5, fill='x', expand=1)
        self.button_prevmonth.pack(side='left', padx=5, pady=5)
        self.subframe_month.pack(side='left', padx=5, pady=5, fill='x', expand=1)
        self.textlabel_currentmonth.pack(side='top')
        self.button_jumptotoday.pack(side='left', padx=5, pady=5)
        self.button_nextmonth.pack(side='left', padx=5, pady=5)

    def changeMonth(self, direction):
        m = self.datevar_month.month
        change = -1 if direction < 0 else 1
        if m == 1 and change == -1:
            mc = 12
            yc = self.datevar_month.year - 1
        elif m == 12 and change == 1:
            mc = 1
            yc = self.datevar_month.year + 1
        else:
            mc = m + change
            yc = self.datevar_month.year
        self.datevar_month = date(yc, mc, 1)
        self.strvar_monthdate.set(value=str(pyra.ReformatDate(date_to_reformat=self.datevar_month,format_type='long',locale='TH', yearsystem='BE').split(sep=' ' ,maxsplit=1)[1]))
    
    def jumptoThisMonth(self):
        self.chosendate=date.today()
        self.datevar_month = date(date.today().year, date.today().month, 1)
        self.strvar_monthdate.set(value=str(pyra.ReformatDate(date_to_reformat=self.datevar_month,format_type='long',locale='TH', yearsystem='BE').split(sep=' ' ,maxsplit=1)[1]))

    @property
    def chosenMonth(self):
        return pyra.encodeDataTimestamp(self.datevar_month,False)[:6]

class SimpleCalendar():
    '''วิตเจ็ตกลุ่มที่ทำหน้าที่เป็นปฏิทินแบบเลื่อนเดือนได้ ประกอบด้วยเฟรมสำหรับเลื่อนเดือน และเฟรมที่มีป้ายวันที่'''
    def __init__(self, master, navigable_date_button=False, secondary_row=False, tertiary_row=False):
        self.stylename_caption ="H3ol.TLabel"
        self.stylename_button = "TButton"
        
        self.ndb = navigable_date_button
        self.sr = secondary_row
        self.tr = tertiary_row

        self.chosendate = date.today()
        self.datevar_month = date(date.today().year, date.today().month, 1)
        self.strvar_monthdate = tk.StringVar(value=str(pyra.ReformatDate(date_to_reformat=self.datevar_month,format_type='long',locale='TH', yearsystem='BE').split(sep=' ' ,maxsplit=1)[1]))
        self.widgetframe = ttk.Frame(master=master)

        self.subframe_monthselector = ttk.Frame(master=self.widgetframe)
        self.button_prevmonth = ttk.Button(master=self.subframe_monthselector, text='◀', style=self.stylename_button, command=lambda:self.changeMonth(-1))
        self.button_jumptotoday = ttk.Button(master=self.subframe_monthselector, text='TODAY', style=self.stylename_button, command=self.jumptoThisMonth)
        self.button_nextmonth = ttk.Button(master=self.subframe_monthselector, text='▶', style=self.stylename_button, command=lambda:self.changeMonth(1))
        self.subframe_month = ttk.Frame(master=self.subframe_monthselector)
        self.textlabel_currentmonth = ttk.Label(master=self.subframe_month, textvariable=self.strvar_monthdate, justify='center', style=self.stylename_caption)

        self.subframe_calendar = ttk.Frame(master=self.widgetframe)
        self.warray_frame_calendar_row = list()         # เก็บแถวปฏิทิน (หนึ่งแถวปฏิทินมีเจ็ดช่อง)
        self.warray_frame_calendar = list()             # เก็บช่องปฏิทิน ภายในแถวปฏิทิน
        self.warray_firstrow = list()                   # เก็บป้ายวันที่ หรือปุ่มวันที่ในปฏิทิน
        self.warray_strvar_day = list()                 # เก็บ StringVar ที่ผูกกับป้ายวันที่ในปฏิทิน
        self.warray_secondrow = list()                  # เก็บป้ายข้อมูลช่องที่ 2 ในปฏิทิน
        self.warray_strvar_secondrow = list()           # เก็บ StringVar ที่ผูกกับป้ายข้อมูลช่องที่ 2 ในปฏิทิน
        self.warray_thirdrow = list()                   # เก็บป้ายข้อมูลช่องที่ 3 ในปฏิทิน
        self.warray_strvar_thirdrow = list()            # เก็บ StringVar ที่ผูกกับป้ายข้อมูลช่องที่ 3 ในปฏิทิน
        self.warray_label_calendarheader = list()       # เก็บป้ายแสดงวันในสัปดาห์ ที่จะแสดงที่แถวแรกของปฏิทิน
        self.cd = 1                                     # ตัวเลขรันสำหรับใช้วางเลขวันที่เฉยๆ
        self.monthstart = False
        self.firstdatofmonth = 0                        # ตัวเลขที่ระบุว่า วันที่ 1 ของเดือน อยู่ที่ดัชนีที่เท่าไหร่

        # วางป้ายวันที่ในสัปดาห์ในแถวแรก... เราจะล็อกให้เริ่มต้นด้วยวันอาทิตย์ไปเลยเพื่อความสะดวกในการเขียน
        self.warray_frame_calendar_row.append(ttk.Frame(master=self.subframe_calendar))
        self.warray_frame_calendar_row[0].pack(side='top', anchor='n', fill='x', expand=1)
        for d in range(0,7):
            self.warray_label_calendarheader.append(ttk.Label(master=self.warray_frame_calendar_row[0], text=pyra.TH_Abbreviated_Weekdays[d]))
            self.warray_label_calendarheader[d].pack(side='left', anchor='n', expand=1)
            self.warray_label_calendarheader[d].configure(style="calendargridnormal.TLabel")
        self.warray_label_calendarheader[0].configure(style="calendargridholiday.TLabel")

        # วางเฟรมย่อยวันที่ แล้ววางตัวควบคุมตามตัวเลือกที่กำหนดให้...
        for row in range(1,7): # กระทำกับแถวที่ 1 ถึงแถวที่ 7 เพราะแถวที่ 0 เป็นวันที่ในสัปดาห์ไปแล้ว...
            self.warray_frame_calendar_row.append(ttk.Frame(master=self.subframe_calendar, style="primary.TFrame"))
            self.warray_frame_calendar_row[row].pack(side='top', anchor='n', fill='x', expand=1)
            for d in range(0,7): # ในแต่ละคอลัมน์... จะวางเฟรมย่อยก่อน แล้วค่อยเติมป้ายหรือปุ่ม...
                self.warray_frame_calendar.append(ttk.Frame(master=self.warray_frame_calendar_row[row], style="cal.TFrame"))
                self.warray_frame_calendar[((row-1)*7)+d].pack(side='left', fill='x', expand=1, anchor='n', padx=1, pady=1)
                self.warray_strvar_day.append(tk.StringVar())

                if navigable_date_button:
                    self.warray_firstrow.append(ttk.Button(master=self.warray_frame_calendar[((row-1)*7)+d], name=str(((row-1)*7)+d), width=1))
                    if d == 0:
                        self.warray_firstrow[((row-1)*7)+d].configure(style="calred.Outline.TButton")
                    else:
                        self.warray_firstrow[((row-1)*7)+d].configure(style="calblack.Outline.TButton")
                else:
                    self.warray_firstrow.append(ttk.Label(master=self.warray_frame_calendar[((row-1)*7)+d], textvariable=self.warray_strvar_day[((row-1)*7)+d], width=1))
                    if d == 0:
                        self.warray_firstrow[((row-1)*7)+d].configure(style="calred.TLabel", justify='right')
                    else:
                        self.warray_firstrow[((row-1)*7)+d].configure(style="calblack.TLabel", justify='right')
                
                # เราจะต้องเริ่มวางวันที่
                if self.monthstart is False:                            # ค่าเริ่มต้นเป็นเท็จ และจะสลับเป็นจริงเมื่อวางวันที่ 1 เรียบร้อยแล้วเท่านั้น
                    if d == 0 and self.datevar_month.weekday() == 6:    # ถ้าหมายเลขวันเป็น 6 (วันอาทิตย์) ให้วางที่ 0
                        self.firstdatofmonth = d
                        self.warray_strvar_day[d].set(self.cd)
                        self.monthstart = not self.monthstart
                        if self.cd == date.today().day and date.today().month == self.datevar_month.month and date.today().year == self.datevar_month.year:
                            if navigable_date_button:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltodayselected.Outline.TButton")
                            else:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltoday.TLabel")
                        self.cd += 1
                    elif d-1 == self.datevar_month.weekday():           # ถ้าคอลัมน์ที่ 1-1 = 0 ตรงกับ 0 (วันจันทร์) เป็นต้นไป ให้วางที่คอลัมน์ d (นั่นก็คือ 1) แยกเงื่อนไขดีกว่าเผื่อกันงง...
                        self.firstdatofmonth = d
                        self.warray_strvar_day[d].set(self.cd)
                        self.monthstart = not self.monthstart
                        if self.cd == date.today().day and date.today().month == self.datevar_month.month and date.today().year == self.datevar_month.year:
                            if navigable_date_button:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltodayselected.Outline.TButton")
                            else:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltoday.TLabel")
                        self.cd += 1
                    else:                                               # ถ้าไม่เข้าเงื่อนไขใดๆ แสดงว่าวันยังมาไม่ถึง ให้ข้ามไปได้เลย
                        self.warray_strvar_day[d].set('')
                else:                                                   # เมื่อวางวันที่ 1 แล้ว จะข้ามมาที่เงื่อนไขนี้ทันที
                    if self.cd <= date(self.datevar_month.year, self.datevar_month.month+1,1).__add__(timedelta(days=-1)).day:
                        self.warray_strvar_day[((row-1)*7)+d].set(self.cd)
                        if self.cd == date.today().day and date.today().month == self.datevar_month.month and date.today().year == self.datevar_month.year:
                            if navigable_date_button:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltodayselected.Outline.TButton")
                            else:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltoday.TLabel")
                        self.cd += 1
                    else:
                        pass
                
                self.warray_firstrow[((row-1)*7)+d].pack(side='top', fill='x')
                if self.ndb:
                    self.assignNav(self.warray_firstrow[((row-1)*7)+d], self.warray_strvar_day[((row-1)*7)+d])
                

                if secondary_row:
                    self.warray_strvar_secondrow.append(tk.StringVar())
                    self.warray_secondrow.append(ttk.Label(master=self.warray_frame_calendar[((row-1)*7)+d], textvariable=self.warray_strvar_secondrow[((row-1)*7)+d], width=1))
                    self.warray_secondrow[((row-1)*7)+d].pack(side='top', fill='x')

                if tertiary_row:
                    self.warray_strvar_thirdrow.append(tk.StringVar())
                    self.warray_thirdrow.append(ttk.Label(master=self.warray_frame_calendar[((row-1)*7)+d], textvariable=self.warray_strvar_thirdrow[((row-1)*7)+d], width=1))
                    self.warray_thirdrow[((row-1)*7)+d].pack(side='top', fill='x')

    def pwpack(self, side, padx=0, pady=0):
        self.widgetframe.pack(side=side, fill='x', expand=0, padx=padx, pady=pady)
        self.subframe_monthselector.pack(side='top', padx=5, pady=5, fill='x', expand=1)
        self.button_prevmonth.pack(side='left', padx=5, pady=5)
        self.subframe_month.pack(side='left', padx=5, pady=5, fill='x', expand=1)
        self.textlabel_currentmonth.pack(side='top')
        self.button_jumptotoday.pack(side='left', padx=5, pady=5)
        self.button_nextmonth.pack(side='left', padx=5, pady=5)
        self.subframe_calendar.pack(side='left', padx=5, pady=5, fill='x', expand=1)

    def changeMonth(self, direction):
        m = self.datevar_month.month
        change = -1 if direction < 0 else 1
        if m == 1 and change == -1:
            mc = 12
            yc = self.datevar_month.year - 1
        elif m == 12 and change == 1:
            mc = 1
            yc = self.datevar_month.year + 1
        else:
            mc = m + change
            yc = self.datevar_month.year
        self.datevar_month = date(yc, mc, 1)
        self.strvar_monthdate.set(value=str(pyra.ReformatDate(date_to_reformat=self.datevar_month,format_type='long',locale='TH', yearsystem='BE').split(sep=' ' ,maxsplit=1)[1]))
        self.repopulateCalendar()

    def jumptoThisMonth(self):
        self.chosendate=date.today()
        self.datevar_month = date(date.today().year, date.today().month, 1)
        self.strvar_monthdate.set(value=str(pyra.ReformatDate(date_to_reformat=self.datevar_month,format_type='long',locale='TH', yearsystem='BE').split(sep=' ' ,maxsplit=1)[1]))
        self.repopulateCalendar()

    def repopulateCalendar(self):
        funccd = 1                    # ตัวเลขรันสำหรับใช้วางเลขวันที่เฉยๆ
        funcmonthstart = False

        for row in range(1,7): # กระทำกับแถวที่ 1 ถึงแถวที่ 7 เพราะแถวที่ 0 เป็นวันที่ในสัปดาห์ไปแล้ว...
            for d in range(0,7): # ในแต่ละคอลัมน์... จะวางเฟรมย่อยก่อน แล้วค่อยเติมป้ายหรือปุ่ม...
                # เราจะต้องเริ่มวางวันที่
                if self.ndb:
                        self.warray_firstrow[((row-1)*7)+d].configure(style="calblack.Outline.TButton")
                else:
                    self.warray_firstrow[((row-1)*7)+d].configure(style="calblack.TLabel")

                if funcmonthstart is False:                            # ค่าเริ่มต้นเป็นเท็จ และจะสลับเป็นจริงเมื่อวางวันที่ 1 เรียบร้อยแล้วเท่านั้น
                    
                    if d == 0 and self.datevar_month.weekday() == 6:    # ถ้าหมายเลขวันเป็น 6 (วันอาทิตย์) ให้วางที่ 0
                        self.firstdatofmonth = d
                        self.warray_strvar_day[d].set(funccd)
                        funcmonthstart = not funcmonthstart
                        if funccd == date.today().day and date.today().month == self.datevar_month.month and date.today().year == self.datevar_month.year:
                            if self.ndb:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltodayselected.Outline.TButton")
                            else:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltoday.TLabel")
                        funccd += 1
                    elif d-1 == self.datevar_month.weekday():           # ถ้าคอลัมน์ที่ 1-1 = 0 ตรงกับ 0 (วันจันทร์) เป็นต้นไป ให้วางที่คอลัมน์ d (นั่นก็คือ 1) แยกเงื่อนไขดีกว่าเผื่อกันงง...
                        self.firstdatofmonth = d
                        self.warray_strvar_day[d].set(funccd)
                        funcmonthstart = not funcmonthstart
                        if funccd == date.today().day and date.today().month == self.datevar_month.month and date.today().year == self.datevar_month.year:
                            if self.ndb:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltodayselected.Outline.TButton")
                            else:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltoday.TLabel")
                        funccd += 1
                    else:                                               # ถ้าไม่เข้าเงื่อนไขใดๆ แสดงว่าวันยังมาไม่ถึง ให้ข้ามไปได้เลย
                        self.warray_strvar_day[d].set('')
                        if self.sr:
                            self.warray_strvar_secondrow[((row-1)*7)+d].set("")
                        if self.tr:
                            self.warray_strvar_thirdrow[((row-1)*7)+d].set("")
                else:                                                   # เมื่อวางวันที่ 1 แล้ว จะข้ามมาที่เงื่อนไขนี้ทันที
                    if funccd <= date(self.datevar_month.year, self.datevar_month.month+1 if self.datevar_month.month < 12 else 1,1).__add__(timedelta(days=-1)).day:
                        self.warray_strvar_day[((row-1)*7)+d].set(funccd)
                        if funccd == date.today().day and date.today().month == self.datevar_month.month and date.today().year == self.datevar_month.year:
                            if self.ndb:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltodayselected.Outline.TButton")
                            else:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="caltoday.TLabel")
                        elif funccd == self.chosendate.day and date.today().month == self.datevar_month.month and date.today().year == self.datevar_month.year:
                            if self.ndb:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="calselected.Outline.TButton")
                            else:
                                self.warray_firstrow[((row-1)*7)+d].configure(style="calselected.TLabel")
                        funccd += 1
                        if self.sr:
                            self.warray_strvar_secondrow[((row-1)*7)+d].set("")
                        if self.tr:
                            self.warray_strvar_thirdrow[((row-1)*7)+d].set("")
                    else:
                        self.warray_strvar_day[((row-1)*7)+d].set('')
                        if self.sr:
                            self.warray_strvar_secondrow[((row-1)*7)+d].set("")
                        if self.tr:
                            self.warray_strvar_thirdrow[((row-1)*7)+d].set("")
                if d == 0:
                    if self.ndb:
                        self.warray_firstrow[((row-1)*7)+d].configure(style="calred.Outline.TButton")
                    else:
                        self.warray_firstrow[((row-1)*7)+d].configure(style="calred.TLabel")
        
    def assignNav(self, target, source):
        '''[INTERNAL METHOD] เมธอดสำหรับกำหนดเป้าหมายการเรียกใช้เมธอด nav ให้กับปุ่มปฏิทิน'''
        target.configure(textvariable=source, command=lambda:self.nav(source,'date'))

    def nav(self, sv, result_format='date'):
        '''[INTERNAL METHOD] คืนค่าวันที่ในรูปแบบ datetime.date หรือแบบสตริงที่อ่านได้ จากการคลิกปุ่มวันที่บนปฏิทิน'''
        try:
            temp = int(sv.get())
        except ValueError:
            return
        self.chosendate = date(self.datevar_month.year, self.datevar_month.month, int(sv.get()))
        if self.ndb:
            for i, bt in enumerate(self.warray_firstrow):
                if self.warray_strvar_day[i].get() == '':
                    continue
                if date(self.datevar_month.year, self.datevar_month.month, int(self.warray_strvar_day[i].get())) == date.today():
                    bt.configure(style="caltoday.Outline.TButton")
                    if self.chosendate == date.today():
                        bt.configure(style="caltodayselected.Outline.TButton")
                elif int(self.warray_strvar_day[i].get()) == int(sv.get()):
                    bt.configure(style="calselected.Outline.TButton")
                else:
                    bt.configure(style="calblack.Outline.TButton")

        if result_format == 'date':
            return date(self.datevar_month.year, self.datevar_month.month, int(sv.get()))
        elif result_format == 'string':
            return pyra.ReformatDate(date_to_reformat=date(self.datevar_month.year, self.datevar_month.month, int(sv.get())), format_type='long', locale='TH', yearsystem='BE')

    def populateSecondRow(self, date_range=[], text_range=[], populating_mode='ra'):
        if populating_mode not in ('ra','r'):
            raise AttributeError("Invalid populating_mode tag. Acceptable tags follow: 'ra' for replace all labels with blank string first, and 'r' for replace only within boundary of input ranges.")
        firstday = False
        if populating_mode == 'ra':
            for sv in self.warray_strvar_secondrow:
                sv.set('')
        for n, d in enumerate(date_range):
            try:
                if not firstday:
                    self.warray_strvar_secondrow[self.firstdatofmonth].set('')
                    if d.day == 1 and d.month == self.datevar_month.month and d.year == self.datevar_month.year:
                        firstday = not firstday
                        self.warray_strvar_secondrow[self.firstdatofmonth].set(text_range[n])
                    else:
                        continue
                else:
                    if d.month == self.datevar_month.month and d.year == self.datevar_month.year:
                        self.warray_strvar_secondrow[self.firstdatofmonth+n].set(text_range[n])
            except ValueError:
                raise ValueError("ค่าในลำดับที่ "+str(n)+" เป็น "+str(d)+" ซึ่งไม่ใช่รูปแบบวันที่ที่ถูกต้อง")

    def populateThirdRow(self, date_range=[], text_range=[], populating_mode='ra'):
        if populating_mode not in ('ra','r'):
            raise AttributeError("Invalid populating_mode tag. Acceptable tags follow: 'ra' for replace all labels with blank string first, and 'r' for replace only within boundary of input ranges.")
        firstday = False
        if populating_mode == 'ra':
            for sv in self.warray_strvar_thirdrow:
                sv.set('')
        for n, d in enumerate(date_range):
            try:
                if not firstday:
                    self.warray_strvar_thirdrow[self.firstdatofmonth].set('')
                    if d.day == 1 and d.month == self.datevar_month.month and d.year == self.datevar_month.year:
                        firstday = not firstday
                        self.warray_strvar_thirdrow[self.firstdatofmonth].set(text_range[n])
                    else:
                        continue
                else:
                    if d.month == self.datevar_month.month and d.year == self.datevar_month.year:
                        self.warray_strvar_thirdrow[self.firstdatofmonth+n].set(text_range[n])
            except ValueError:
                raise ValueError("ค่าในลำดับที่ "+str(n)+" เป็น "+str(d)+" ซึ่งไม่ใช่รูปแบบวันที่ที่ถูกต้อง")

    @property
    def date(self):
        return self.chosendate
    
class DetailsPane():
    '''วิตเจ็ตกลุ่มที่ประกอบด้วยป้ายกำกับด้านซ้าย และป้ายแสดงข้อมูลด้านขวา ใช้สำหรับแสดงข้อมูลรายละเอียดอย่างง่าย'''
    def __init__(self):
        pass

class DateEntry():
    '''วิดเจ็ตกลุ่มที่ประกอบด้วยกล่องข้อความสำหรับกรอกตัวเลขปี และดรอปดาวน์สำหรับเลือกเดือนและวันที่\n
    โดยการเลือกปีและเดือนจะกรองวันที่ที่เป็นไปได้ให้โดยอัตโนมัติ สามารถตั้งค่าให้แสดงป้ายกำกับเพิ่มเติมที่ด้านบนหรือด้านล่างเพิ่มเติม'''
    def __init__(self, master, datevar, including_label_position='off', entry_order='dmy', entry_format='number', yearsystem='AD'):
        if including_label_position not in ('off', 'top', 'bottom','inline'):
            raise AttributeError("Invalid including_label_position tag. Acceptable tags follow: 'off' to show only entry boxes, 'top' to show labels above each box, 'bottom' to show labels below each box, or 'inline' to show labels before each box.")
        if entry_order not in ('dmy', 'ymd'):
            raise AttributeError("Invalid entry_order tag.")
        if entry_format not in ('number', 'word'):
            raise AttributeError("Invalid entry_format tag.")
        if yearsystem not in ('AD', 'BE'):
            raise AttributeError("Invalid yearsystem tag.")
        
        self.pos = including_label_position
        self.order = entry_order
        self.ys = yearsystem

        self.currentdate = datevar
        self.intvar_day = tk.IntVar(value=self.currentdate.day)
        self.intvar_month = tk.IntVar(value=self.currentdate.month)
        self.intvar_year = tk.IntVar(value=self.currentdate.year+543 if self.ys == 'BE' else self.currentdate.year)

        self.widgetframe = ttk.Frame(master=master)
        self.subframe_year = ttk.Frame(master=self.widgetframe)
        self.subframe_month = ttk.Frame(master=self.widgetframe)
        self.subframe_day = ttk.Frame(master=self.widgetframe)
        if including_label_position != 'off':
            self.label_year = ttk.Label(master=self.subframe_year, text='ปี ', style="form.TLabel")
            self.label_month = ttk.Label(master=self.subframe_month, text='เดือน ', style="form.TLabel")
            self.label_day = ttk.Label(master=self.subframe_day, text='วัน ', style="form.TLabel")
        
        self.spbx_year = ttk.Spinbox(master=self.subframe_year, textvariable=self.intvar_year, width=6, from_=2500 if yearsystem == 'BE' else 1900, to=3000 if yearsystem == 'BE' else 2400, command=self.setDayRange, style="TSpinbox")
        self.spbx_year.bind('<Key>', 'break')
        if entry_format == 'word':
            self.ctrl_month = ttk.Combobox(master=self.subframe_month, values=pyra.TH_Full_Months, width=15, style="TCombobox")
            self.ctrl_month.bind('<Key>', 'break')
            self.ctrl_month.bind('<<ComboboxSelected>>', lambda e:self.setDayRange())
            self.setMonthWord(src='var', dst='ctrl')
        else:
            self.ctrl_month = ttk.Spinbox(master=self.subframe_month, textvariable=self.intvar_month, width=6, from_=1, to=12, command=self.setDayRange)
            self.ctrl_month.bind('<Key>', 'break')
        self.spbx_day = ttk.Spinbox(master=self.subframe_day, textvariable=self.intvar_day, width=6, from_=1, to=31, wrap=True, style="TSpinbox")
        self.spbx_day.bind('<Key>', 'break')
        self.setDayRange()

    @property
    def daybox(self):
        return self.intvar_day
    
    @property
    def monthbox(self):
        return self.intvar_month
    
    @property
    def yearbox(self):
        return self.intvar_year

    @property
    def chosenDate(self):
        return date(self.intvar_year.get()-543 if self.ys == 'BE' else self.intvar_year.get(), self.intvar_month.get(), self.intvar_day.get())

    def setMonthWord(self, src, dst):
        if src == 'var' and dst == 'ctrl':
            self.ctrl_month.set(pyra.TH_Full_Months[self.intvar_month.get()-1])
        elif src == 'ctrl' and dst == 'var':
            self.intvar_month.set(pyra.TH_Full_Months.index(self.ctrl_month.get())+1)
        else:
            raise AttributeError("Invalid direction. Use src='var' and dst='ctrl' to apply month from IntVar to Combobox, and use src='ctrl' and dst='var' for vice versa.")

    def updateDate(self,source_date):
        self.intvar_day.set(source_date.day)
        self.intvar_month.set(source_date.month)
        self.intvar_year.set(source_date.year)

    def setDayRange(self):
        self.setMonthWord(src='ctrl', dst='var')
        if self.intvar_month.get() == 2:
            if self.intvar_year.get() % 4 == 0:
                if not(self.intvar_year.get() % 400 == 0) and self.intvar_year.get() % 100 == 0:
                    if self.intvar_day.get() > 28:
                        self.intvar_day.set(28)
                    self.spbx_day.configure(to=28)
                else:
                    if self.intvar_day.get() > 29:
                        self.intvar_day.set(29)
                    self.spbx_day.configure(to=29)
            else:
                if self.intvar_day.get() > 28:
                    self.intvar_day.set(28)
                self.spbx_day.configure(to=28)
        elif self.intvar_month.get() in (1,3,5,7,8,10,12):
            self.spbx_day.configure(to=31)
        else:
            if self.intvar_day.get() > 30:
                self.intvar_day.set(30)
            self.spbx_day.configure(to=30)
        # อ่านเดือน และปี เพื่อกำหนดช่วงเลขวันที่สามารถเลื่อนไปมาได้
        # โดย หากตัวเลือกแสดงเดือนเป็น word จะต้องมีฟังก์ชันอ่านข้อความเดือน แล้วคืน ดัชนี+1 จากทูเปิลไปเก็บใน IntVar
        # แล้วค่อยคำนวณว่า...
        # 1. ถ้า intvar_month เป็น 1, 3, 5, 7, 8, 10, 12 ให้ช่วงสำหรับ spbx_day เป็น range(1,32)
        # 2. ถ้า intvar_month เป็น 2 ให้ตรวจสอบว่า intvar_year หารด้วย 4 ลงตัว -> range(1,29) ถ้า intvar_year หาร 400 ไม่ลงตัว และหาร 100 ลงตัว นอกจากนั้น ให้ range(1,30) นอกจากนั้นให้ range(1,29)
        # นอกจากนั้นให้เป็น range(1,31)
        # อันนี้จะต้องทริกเกอร์ทุกครั้งที่ค่าในช่องใดๆ มีการเปลี่ยนแปลง

    def pwpack(self, side, padx=0, pady=0, fill=True, expand=0):
        self.widgetframe.pack(side=side, padx=padx, pady=pady, fill='x' if fill else 'none', expand=expand)
        if self.order == 'ymd':
            self.subframe_year.pack(side='left', fill='x' if fill else 'none', expand=expand, padx=5)
            self.subframe_month.pack(side='left', fill='x' if fill else 'none', expand=expand)
            self.subframe_day.pack(side='left', fill='x' if fill else 'none', expand=expand, padx=5)
        else:
            self.subframe_day.pack(side='left', fill='x' if fill else 'none', expand=expand, padx=5)
            self.subframe_month.pack(side='left', fill='x' if fill else 'none', expand=expand)
            self.subframe_year.pack(side='left', fill='x' if fill else 'none', expand=expand, padx=5)
        
        if self.pos == 'off':
            self.spbx_year.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.ctrl_month.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.spbx_day.pack(side='top', fill='x' if fill else 'none', expand=expand)
        elif self.pos == 'top':
            self.label_year.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.label_month.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.label_day.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.spbx_year.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.ctrl_month.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.spbx_day.pack(side='top', fill='x' if fill else 'none', expand=expand)
        elif self.pos == 'bottom':
            self.spbx_year.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.ctrl_month.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.spbx_day.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.label_year.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.label_month.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.label_day.pack(side='top', fill='x' if fill else 'none', expand=expand)
        elif self.pos == 'inline':
            self.label_year.pack(side='left', fill='y' if fill else 'none', expand=expand)
            self.label_month.pack(side='left', fill='y' if fill else 'none', expand=expand)
            self.label_day.pack(side='left', fill='y' if fill else 'none', expand=expand)
            self.spbx_year.pack(side='left', fill='y' if fill else 'none', expand=expand)
            self.ctrl_month.pack(side='left', fill='y' if fill else 'none', expand=expand)
            self.spbx_day.pack(side='left', fill='y' if fill else 'none', expand=expand)

class TimeEntry():
    '''วิดเจ็ตกลุ่มที่ประกอบด้วยดรอปดาวน์สำหรับเลือกชั่วโมง นาที และวินาที\n
    สามารถตั้งค่าให้แสดงป้ายกำกับเพิ่มเติมที่ด้านบนหรือด้านล่างเพิ่มเติม'''
    def __init__(self, master, timevar: time, including_label_position='off', include_second=False):
        if including_label_position not in ('off', 'top', 'bottom','inline'):
            raise AttributeError("Invalid including_label_position tag. Acceptable tags follow: 'off' to show only entry boxes, 'top' to show labels above each box, 'bottom' to show labels below each box, or 'inline' to show labels before each box.")
        
        self.pos = including_label_position
        self.enable_second = include_second

        self.currenttime = timevar
        self.intvar_hour = tk.IntVar(value=self.currenttime.hour)
        self.intvar_minute = tk.StringVar(value=self.currenttime.minute)
        self.intvar_second = tk.StringVar(value=self.currenttime.second)

        self.widgetframe = ttk.Frame(master=master)
        self.subframe_hour = ttk.Frame(master=self.widgetframe)
        self.subframe_minute = ttk.Frame(master=self.widgetframe)
        self.subframe_second = ttk.Frame(master=self.widgetframe)
        if including_label_position != 'off':
            self.label_hour = ttk.Label(master=self.subframe_hour, text='ชั่วโมง ', style="form.TLabel")
            self.label_minute = ttk.Label(master=self.subframe_minute, text='นาที ', style="form.TLabel")
            self.label_second = ttk.Label(master=self.subframe_second, text='วินาที ', style="form.TLabel")
        
        self.spbx_hour = ttk.Spinbox(master=self.subframe_hour, textvariable=self.intvar_hour, width=6, from_=0, to=23, wrap=True, style="TSpinbox")
        self.spbx_hour.bind('<Key>', 'break')
        self.spbx_minute = ttk.Spinbox(master=self.subframe_minute, textvariable=self.intvar_minute, width=6, values=[f"{n:02}" for n in range(0,60)], wrap=True, style="TSpinbox")
        self.spbx_minute.bind('<Key>', 'break')
        self.spbx_second = ttk.Spinbox(master=self.subframe_second, textvariable=self.intvar_second, width=6, values=[f"{n:02}" for n in range(0,60)], wrap=True, style="TSpinbox")
        self.spbx_second.bind('<Key>', 'break')

        

    @property
    def hourbox(self):
        return self.intvar_hour
    
    @property
    def minutebox(self):
        return self.intvar_minute
    
    @property
    def secondbox(self):
        return self.intvar_second

    @property
    def chosenTime(self):
        return time(self.intvar_hour.get(), int(self.intvar_minute.get()), int(self.intvar_second.get()))

    def updateTime(self,source_time:time):
        self.intvar_day.set(source_time.hour)
        self.intvar_month.set(f"{source_time.minute:02}")
        self.intvar_year.set(f"{source_time.second:02}")

    def pwpack(self, side, padx=0, pady=0, fill=True, expand=0):
        self.widgetframe.pack(side=side, padx=padx, pady=pady, fill='x' if fill else 'none', expand=expand)
        self.subframe_hour.pack(side='left', fill='x' if fill else 'none', expand=expand, padx=5)
        self.subframe_minute.pack(side='left', fill='x' if fill else 'none', expand=expand)
        self.subframe_second.pack(side='left', fill='x' if fill else 'none', expand=expand, padx=5)
        
        if self.pos == 'off':
            self.spbx_hour.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.spbx_minute.pack(side='top', fill='x' if fill else 'none', expand=expand)
            if self.enable_second:
                self.spbx_second.pack(side='top', fill='x' if fill else 'none', expand=expand)
        elif self.pos == 'top':
            self.label_hour.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.label_minute.pack(side='top', fill='x' if fill else 'none', expand=expand)
            if self.enable_second:
                self.label_second.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.spbx_hour.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.spbx_minute.pack(side='top', fill='x' if fill else 'none', expand=expand)
            if self.enable_second:
                self.spbx_second.pack(side='top', fill='x' if fill else 'none', expand=expand)
        elif self.pos == 'bottom':
            self.spbx_hour.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.spbx_minute.pack(side='top', fill='x' if fill else 'none', expand=expand)
            if self.enable_second:
                self.spbx_second.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.label_hour.pack(side='top', fill='x' if fill else 'none', expand=expand)
            self.label_minute.pack(side='top', fill='x' if fill else 'none', expand=expand)
            if self.enable_second:
                self.label_second.pack(side='top', fill='x' if fill else 'none', expand=expand)
        elif self.pos == 'inline':
            self.label_hour.pack(side='left', fill='y' if fill else 'none', expand=expand)
            self.label_minute.pack(side='left', fill='y' if fill else 'none', expand=expand)
            if self.enable_second:
                self.label_second.pack(side='left', fill='y' if fill else 'none', expand=expand)
            self.spbx_hour.pack(side='left', fill='y' if fill else 'none', expand=expand)
            self.spbx_minute.pack(side='left', fill='y' if fill else 'none', expand=expand)
            if self.enable_second:
                self.spbx_second.pack(side='left', fill='y' if fill else 'none', expand=expand)

class FormField():
    '''
    ช่องกรอกข้อมูลกึ่งสำเร็จรูปที่จัดให้เป็นโครงสร้างมาตรฐาน
    '''
    def __init__(self, master, caption_text: str, contains_secondary_caption=False, secondary_caption=""):
        self.widgetframe = tk.Frame(master=master, relief='raised')
        self.lbl_upper_caption = ttk.Label(master=self.widgetframe, text=caption_text)
        if contains_secondary_caption:
            if len(secondary_caption) < 1:
                raise ValueError("When 'contains_secondary_caption' is set to True, you must provide at least one string for secondary caption.")
            else:
                self.lbl_secondary_caption = ttk.Label(master=self.widgetframe, text=secondary_caption)

class EntryField(FormField):
    def __init__(self, master, caption_text: str, target_var: tk.Variable, width:int=10, contains_secondary_caption=False, apply_mask=False, read_only=False, secondary_caption=""):
        super().__init__(master,caption_text,contains_secondary_caption, secondary_caption)
        self.target_var = target_var
        self.input = ttk.Entry(master=self.widgetframe,style="success.TEntry" if not read_only else "visdata.TEntry", textvariable=target_var, width=width)
        if apply_mask:
            self.input.configure(show='*') 
        if read_only:
            self.input.bind('<Key>','break')

    def pwpack(self, side, fill, anchor, padx, pady):
        self.widgetframe.pack(side=side, fill=fill, anchor=anchor, padx=padx, pady=pady)
        self.lbl_upper_caption.pack(side='top', fill='x', anchor='n')
        self.input.pack(side='top', fill='x', anchor='n')
        try:
            self.lbl_secondary_caption.pack(side='top', fill='x', anchor='n')
        except AttributeError:
            pass

    def pwgrid(self, row_slot, column_slot, row_span=1, column_span=1, padx=0, pady=0, cell_anchor='nw'):
        self.widgetframe.grid(row=row_slot, column=column_slot, rowspan=row_span, columnspan=column_span, sticky=cell_anchor, padx=padx, pady=pady)
        self.lbl_upper_caption.pack(side='top', fill='x', anchor='n')
        self.input.pack(side='top', fill='x', anchor='n')
        try:
            self.lbl_secondary_caption.pack(side='top', fill='x', anchor='n')
        except AttributeError:
            pass

    @property
    def currentValue(self):
        return self.target_var.get()
    
class ComboField(FormField):
    def __init__(self,master, caption_text: str, target_var: tk.Variable, width:int=10, contains_secondary_caption=False, read_only=False, values: list[str] | tuple[str,...]=[], secondary_caption=""):
        super().__init__(master,caption_text,contains_secondary_caption, secondary_caption)
        self.target_var = target_var
        self.input = ttk.Combobox(master=self.widgetframe, textvariable=target_var, style="success.TCombobox" if not read_only else "visdata.TCombobox", values=values, width=width)
        if read_only:
            self.input.bind('<Key>','break')

    def pwpack(self, side, fill, anchor, padx, pady):
        self.widgetframe.pack(side=side, fill=fill, anchor=anchor, padx=padx, pady=pady)
        self.lbl_upper_caption.pack(side='top', fill='x', anchor='n')
        self.input.pack(side='top', fill='x', anchor='n')
        try:
            self.lbl_secondary_caption.pack(side='top', fill='x', anchor='n')
        except AttributeError:
            pass
    @property
    def currentValue(self):
        return self.target_var.get()
    
class SpinField(FormField):
    def __init__(self, master, caption_text:str, target_var: tk.Variable, width:int=10, contains_secondary_caption=False, read_only=False, bottom_value: float =0.0, top_value: float=10.0, step:float=1.0, secondary_caption=""):
        super().__init__(master,caption_text,contains_secondary_caption, secondary_caption)
        self.target_var = target_var
        self.input = ttk.Spinbox(master=self.widgetframe, textvariable=target_var, style="success.TSpinbox" if not read_only else "visdata.TSpinbox", width=width, from_=bottom_value, to=top_value, increment=step)
        if read_only:
            self.input.bind('<Key>','break')

    def pwpack(self, side, fill, anchor, padx, pady):
        self.widgetframe.pack(side=side, fill=fill, anchor=anchor, padx=padx, pady=pady)
        self.lbl_upper_caption.pack(side='top', fill='x', anchor='n')
        self.input.pack(side='top', fill='x', anchor='n')
        try:
            self.lbl_secondary_caption.pack(side='top', fill='x', anchor='n')
        except AttributeError:
            pass
        
    @property
    def currentValue(self):
        return self.target_var.get()