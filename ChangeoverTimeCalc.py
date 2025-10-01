import tkinter as tk
import tkinter.ttk as ttk
import pyra
from ttkbootstrap import Style
from tkinter import messagebox
from datetime import date, time, datetime, timedelta

TH_Full_Weekdays = ("วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์")
TH_Abbreviated_Weekdays = ("อา.", "จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส.")
TH_Full_Months = ("มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม")
TH_Abbreviated_Months = ("ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ย.", "ส.ค", "ก.ค", "ต.ค.", "พ.ย.", "ธ.ค.")

EN_Full_Weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
EN_Abbreviated_Weekdays = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
EN_Symbol_Weekdays = ("S", "M", "T", "W", "T", "F", "S")
EN_Full_Months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
EN_Abbreviated_Months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


tuple_spinner_morning = ('7.00','7.15','7.30','7.45','8.00','8.15','8.30','8.45','9.00')
tuple_spinner_afternoon = ('11.00','11.15','11.30','11.45','12.00','12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00')
tuple_spinner_evening = ('16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30')
tuple_spinner_overtimebegins = ('None','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30')
tuple_spinner_overtimeends = ('None','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00')

#region Style Settings
Style = Style("yeti")
baseui_FontSize = 8
baseui_LatinFont = "Arial"
baseui_ThaiFont = "Arial"
baseui_language = "EN"
mono_FontSize = 10
mono_Font = "Segoe UI"
baseui_Font = baseui_ThaiFont if baseui_language == "TH" else baseui_LatinFont

Style.configure("TLabel",font=(baseui_Font, baseui_FontSize),padding=1)
Style.configure("TEntry",padding=3)
Style.configure("Toolbutton",padding=3)
Style.configure("TSpinbox",arrowsize=1,padding=2, arrowcolor="#B1B1B1")
Style.configure("TCombobox",padding=3)
Style.configure("title.TLabel",font=(baseui_Font, baseui_FontSize+2, 'bold'),foreground="#ffffff",background="#141313")
Style.configure("titleLight.TLabel",font=(baseui_Font, baseui_FontSize+2, 'bold'),padding=(2,2),foreground="#000000",background="#B9AFAF")
Style.configure("h1.TLabel",font=(mono_Font, baseui_FontSize*2, 'bold'),background="#ffa620")
Style.configure("h2.TLabel",font=(baseui_Font, int(baseui_FontSize*1.2)))
Style.configure("TButton",font=(baseui_Font, baseui_FontSize))
Style.configure("doublesized.TLabel",font=(baseui_Font, baseui_FontSize*2))
Style.configure("dashboard.Treeview",font=(mono_Font, mono_FontSize+2, 'bold'), rowheight=75)
Style.configure("dashboard.Treeview.Heading",font=(mono_Font, mono_FontSize))
Style.configure("dashboard.Treeview.Cell",padding=5)
Style.configure("Treeview", rowheight=25)
Style.configure("Treeview.Heading",relief="ridge")
Style.configure("primary.Treeview", rowheight=25)
Style.configure("warning.Treeview", rowheight=25)
#endregion


class DateTimeVar():
    def __init__(self, date_time:datetime = datetime.now(), detect_changes:bool=False):
        '''sdfsdf'''
        self.value = date_time
        self.var_Year = tk.IntVar(value=date_time.year)
        self.var_Month = tk.IntVar(value=date_time.month)
        self.var_Day = tk.IntVar(value=date_time.day)
        self.var_Hour = tk.IntVar(value=date_time.hour)
        self.var_Minute = tk.IntVar(value=date_time.minute)
        self.var_Second = tk.IntVar(value=date_time.second)

        if detect_changes:
            self.var_Year.trace_add(mode='write',callback=lambda x,y,z :self.get_datetime())
            self.var_Month.trace_add(mode='write',callback=lambda x,y,z :self.get_datetime())
            self.var_Day.trace_add(mode='write',callback=lambda x,y,z :self.get_datetime())
            self.var_Hour.trace_add(mode='write',callback=lambda x,y,z :self.get_datetime())
            self.var_Minute.trace_add(mode='write',callback=lambda x,y,z :self.get_datetime())
            self.var_Second.trace_add(mode='write',callback=lambda x,y,z :self.get_datetime())

    def get_datetime(self):
        try:
            return datetime(self.var_Year.get(),self.var_Month.get(),self.var_Day.get(),self.var_Hour.get(),self.var_Minute.get(),self.var_Second.get())
        except ValueError:
            return

class LinearDateSelector():
    def __init__(
        self,
        master,
        frame_title:str,
        variable:DateTimeVar,
        type:str = 'date',
        monthSelectorType:str = 'long',
        locale_date:str = 'TH',
        locale_ui:str = 'TH',
        value_order:str = 'dmy',
        spinbox_size:int = 10,
        combobox_size:int = 20,
        use_CustomStyle:bool = False,
        customStyle:str = ''):


        self.monthFormat = monthSelectorType
        self.var_longmonth = tk.StringVar()
        self.locale = locale_date

        self.masterframe = ttk.LabelFrame(master,text=frame_title)
        self.margin = ttk.Frame(self.masterframe)
        self.margin.pack(padx=3,pady=3,fill='both')
        self.frame_Date = ttk.Frame(self.margin)
        self.frame_Time = ttk.Frame(self.margin)
        self.lbl_day = ttk.Label(self.frame_Date,text="วันที่" if locale_ui == 'TH' else "Date")
        self.lbl_month = ttk.Label(self.frame_Date,text="เดือน" if locale_ui == 'TH' else "Date")
        self.lbl_year = ttk.Label(self.frame_Date,text="ปี" if locale_ui == 'TH' else "Date")
        self.lbl_hour = ttk.Label(self.frame_Time,text="ชั่วโมง" if locale_ui == 'TH' else "Hour")
        self.lbl_minute = ttk.Label(self.frame_Time,text="นาที" if locale_ui == 'TH' else "Minute")
        self.lbl_second = ttk.Label(self.frame_Time,text="วินาที" if locale_ui == 'TH' else "Second")
        self.ctrl_day = ttk.Spinbox(self.frame_Date, from_=1,to=31, width=spinbox_size, textvariable=variable.var_Day,wrap=True)
        self.ctrl_shortmonth = ttk.Spinbox(self.frame_Date,text="วันที่" if locale_ui == 'TH' else "Date", from_=1,to=12, width=spinbox_size, textvariable=variable.var_Month,wrap=True)
        self.ctrl_longmonth = ttk.Combobox(self.frame_Date, width=combobox_size, textvariable=self.var_longmonth, values=TH_Full_Months if locale_date == 'TH' else EN_Full_Months)
        self.ctrl_longmonth.bind('<<ComboboxSelected>>',lambda x:self.onComboChange(variable))
        self.ctrl_year = ttk.Spinbox(self.frame_Date, from_=1000,to=3000, width=spinbox_size, textvariable=variable.var_Year, wrap=True, command=lambda:self.recorrectDays(variable))
        self.ctrl_hour = ttk.Spinbox(self.frame_Time, from_=0, to=23, width=spinbox_size, textvariable=variable.var_Hour, wrap=True)
        self.ctrl_minute = ttk.Spinbox(self.frame_Time, from_=0, to=59, width=spinbox_size, textvariable=variable.var_Minute, wrap=True)
        self.ctrl_second = ttk.Spinbox(self.frame_Time, from_=0, to=59, width=spinbox_size, textvariable=variable.var_Second, wrap=True)

        self.ctrl_day.bind("<MouseWheel>","break")
        self.ctrl_shortmonth.bind("<MouseWheel>","break")
        self.ctrl_year.bind("<MouseWheel>","break")
        self.ctrl_hour.bind("<MouseWheel>","break")
        self.ctrl_minute.bind("<MouseWheel>","break")
        self.ctrl_second.bind("<MouseWheel>","break")

        if type.find("date") != -1:
            self.frame_Date.pack(fill='x')
            self.lbl_day.grid(row=0,column=value_order.index('d'),padx=0,pady=0,sticky='w')
            self.lbl_month.grid(row=0,column=value_order.index('m'),padx=0,pady=0,sticky='w')
            self.lbl_year.grid(row=0,column=value_order.index('y'),padx=0,pady=0,sticky='w')
            self.ctrl_day.grid(row=1,column=value_order.index('d'),padx=2,pady=0)
            self.ctrl_year.grid(row=1,column=value_order.index('y'),padx=2,pady=0)
            if monthSelectorType == 'long':
                self.ctrl_longmonth.grid(row=1,column=value_order.index('m'),padx=2,pady=0)
            else:
                self.ctrl_shortmonth.grid(row=1,column=value_order.index('m'),padx=2,pady=0)
        if type.find("time") != -1:
            self.frame_Time.pack(fill='x')
            self.lbl_hour.grid(row=0,column=3,padx=0,pady=0,sticky='w')
            self.lbl_minute.grid(row=0,column=4,padx=0,pady=0,sticky='w')
            self.lbl_second.grid(row=0,column=5,padx=0,pady=0,sticky='w')
            self.ctrl_hour.grid(row=1,column=3,padx=2,pady=2)
            self.ctrl_minute.grid(row=1,column=4,padx=2,pady=2)
            self.ctrl_second.grid(row=1,column=5,padx=2,pady=2)

        self.setLongMonth(variable)
        self.recorrectDays(variable)
        
    def pack(self, side='top', fill='none', anchor='n', padx=0, pady=0):
        self.masterframe.pack(side=side,fill=fill,anchor=anchor,padx=padx,pady=pady,ipadx=5,ipady=5)

    def setLongMonth(self,variable:DateTimeVar):
        self.var_longmonth.set(TH_Full_Months[variable.var_Month.get()-1] if self.locale == 'TH' else EN_Full_Months.index[variable.var_Month.get()-1])

    def onComboChange(self,variable:DateTimeVar):
        # try:
        variable.var_Month.set(TH_Full_Months.index(self.var_longmonth.get())+1 if self.locale == 'TH' else EN_Full_Months.index(self.var_longmonth.get())+1)
        self.recorrectDays(variable)
        # except:
        #     print("ERROR at onComboChange")
        
    def recorrectDays(self,variable:DateTimeVar):
        '''Adjust range of days available in day selector to match month and leap year constraints.'''
        y = variable.var_Year.get()
        m = variable.var_Month.get()
        d = variable.var_Day.get()
        if m == 2:
            if y % 4 == 0:
                if y % 100 == 0:
                    if y % 400 == 0:
                        self.ctrl_day.configure(to=29)
                        if d > 29:
                            variable.var_Day.set(29)
                    else:
                        self.ctrl_day.configure(to=28)
                        if d > 28:
                            variable.var_Day.set(28)
                else:
                    self.ctrl_day.configure(to=29)
                    if d > 29:
                        variable.var_Day.set(29)
            else:
                self.ctrl_day.configure(to=28)
                if d > 28:
                        variable.var_Day.set(28)
        elif m in (4,6,9,11):
            self.ctrl_day.configure(to=30)
            if d > 30:
                variable.var_Day.set(30)
        else:
            self.ctrl_day.configure(to=31)
            
class LocalChangeoverDate():
    def __init__(self,container,column:int,offset:int):
        self.Date = tk.StringVar()
        self.DayofWeek = tk.StringVar()
        self.MorningShiftBegins = tk.StringVar(value='8.00')
        self.MorningShiftEnds = tk.StringVar(value='12.00')
        self.AfternoonBegins = tk.StringVar(value='13.00')
        self.ShiftEnds = tk.StringVar(value='17.00')
        self.OvertimeBegins = tk.StringVar(value='None')
        self.OvertimeEnds = tk.StringVar(value='None')
        self.ExcludedTime = tk.IntVar(value=0)
        self.IsHoliday = tk.BooleanVar(value=False)
        self.LocalThroughputTime = tk.IntVar(value=0)
        self.LocalChangeoverTime = tk.IntVar(value=0)

        self.ctrl_ColumnID = ttk.Label(container, text=column, justify='center', width=5)
        self.ctrl_Date = ttk.Entry(container, textvariable=self.Date, width=5)
        self.ctrl_Date.bind('<Key>',"break")
        self.ctrl_Date.bind('<Button-1>',"break")
        self.ctrl_DayOfWeek = ttk.Entry(container, textvariable=self.DayofWeek, width=5)
        self.ctrl_DayOfWeek.bind('<Key>',"break")
        self.ctrl_DayOfWeek.bind('<Button-1>',"break")
        self.ctrl_IsHoliday = ttk.Checkbutton(container, variable=self.IsHoliday, text='หยุด', width=5, command=lambda:self.setHolidayFieldLock(), style='danger.Toolbutton', state='disabled')
        self.ctrl_MorningBegins = ttk.Spinbox(container, textvariable=self.MorningShiftBegins, width=5, values=tuple_spinner_morning, state='disabled')
        self.ctrl_MorningEnds = ttk.Spinbox(container, textvariable=self.MorningShiftEnds, width=5, values=tuple_spinner_afternoon, state='disabled')
        self.ctrl_AfternoonBegins = ttk.Spinbox(container, textvariable=self.AfternoonBegins, width=5, values=tuple_spinner_afternoon, state='disabled')
        self.ctrl_AfternoonEnds = ttk.Spinbox(container, textvariable=self.ShiftEnds, width=5, values=tuple_spinner_evening, state='disabled')
        self.ctrl_OvertimeBegins = ttk.Spinbox(container, textvariable=self.OvertimeBegins, width=5, values=tuple_spinner_overtimebegins, state='disabled')
        self.ctrl_OvertimeEnds = ttk.Spinbox(container, textvariable=self.OvertimeEnds, width=5, values=tuple_spinner_overtimeends, state='disabled')
        self.ctrl_ExcludedTime = ttk.Spinbox(container, textvariable=self.ExcludedTime, width=5, from_=0, to=600, increment=15, state='disabled')
        self.ctrl_LocalThroughput = ttk.Entry(container, textvariable=self.LocalThroughputTime, width=7, state='disabled')
        self.ctrl_LocalChangeover = ttk.Entry(container, textvariable=self.LocalChangeoverTime, width=7, state='disabled')

        self.ctrl_ColumnID.grid(row=0,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_Date.grid(row=1,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_DayOfWeek.grid(row=2,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_IsHoliday.grid(row=3,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_MorningBegins.grid(row=4,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_MorningEnds.grid(row=5,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_AfternoonBegins.grid(row=6,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_AfternoonEnds.grid(row=7,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_OvertimeBegins.grid(row=8,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_OvertimeEnds.grid(row=9,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_ExcludedTime.grid(row=10,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_LocalThroughput.grid(row=11,column=column+offset,padx=0,pady=0,sticky='nsew')
        self.ctrl_LocalChangeover.grid(row=12,column=column+offset,padx=0,pady=0,sticky='nsew')

    def setHolidayFieldLock(self):
        self.ctrl_MorningBegins.configure(state='disabled' if self.IsHoliday.get() else 'normal')
        self.ctrl_MorningEnds.configure(state='disabled' if self.IsHoliday.get() else 'normal')
        self.ctrl_AfternoonBegins.configure(state='disabled' if self.IsHoliday.get() else 'normal')
        self.ctrl_AfternoonEnds.configure(state='disabled' if self.IsHoliday.get() else 'normal')
        self.ctrl_OvertimeBegins.configure(state='disabled' if self.IsHoliday.get() else 'normal')
        self.ctrl_OvertimeEnds.configure(state='disabled' if self.IsHoliday.get() else 'normal')
        self.ctrl_ExcludedTime.configure(state='disabled' if self.IsHoliday.get() else 'normal')
        self.ctrl_LocalThroughput.configure(state='disabled' if self.IsHoliday.get() else 'normal')
        self.ctrl_LocalChangeover.configure(state='disabled' if self.IsHoliday.get() else 'normal')


class App():

    def __init__(self, rt, title):
        #region Variables
        self.array_CalculationDates = list()
        self.default_MorningShiftBegins = tk.StringVar(value='8.00')
        self.default_MorningShiftEnds = tk.StringVar(value='12.00')
        self.default_AfternoonBegins = tk.StringVar(value='13.00')
        self.default_AfternoonEnds = tk.StringVar(value='17.00')
        self.total_ThroughputTime = tk.IntVar()
        self.total_ChangeoverTime = tk.IntVar()

        #endregion
        #region Basics
        self.windowRoot = rt
        self.windowRoot.title(title)
        self.windowRoot.geometry('1240x635')
        self.windowRoot.minsize(1240,635)
        self.windowRoot.resizable(1,1)

        self.frame_Title = ttk.Frame(self.windowRoot)
        self.frame_Title.pack(side='top',fill='x',anchor='n')
        self.frame_Content = ttk.Frame(self.windowRoot)
        self.frame_Content.pack(side='top',fill='x',anchor='n',padx=5,pady=5)
        self.frame_EventTimes = ttk.Frame(self.frame_Content)
        self.frame_EventTimes.pack(side='left',fill='y',anchor='n',padx=5,pady=5)
        self.frame_Calculation = ttk.Frame(self.frame_Content)
        self.frame_Calculation.pack(side='left',fill='both',expand=True,anchor='n',padx=5,pady=5)

        self.lbl_Title = ttk.Label(self.frame_Title, text=" โปรแกรมคำนวณเวลาการเปลี่ยนสไตล์งาน",style="h1.TLabel")
        self.lbl_Title.pack(fill='x',ipadx=20,ipady=5)

        self.var_PreviousStyleEndDate = DateTimeVar(detect_changes=True)
        self.PreviousStyleEndDate = LinearDateSelector(self.frame_EventTimes,frame_title="  วัน/เวลาที่ตรวจงานตัวสุดท้ายของสไตล์เดิม  ",type="datetime",variable=self.var_PreviousStyleEndDate)
        self.PreviousStyleEndDate.pack(side='top',padx=3,pady=3)

        self.var_CurrentStyleStartDate = DateTimeVar(detect_changes=True)
        self.CurrentStyleStartDate = LinearDateSelector(self.frame_EventTimes,frame_title="  วัน/เวลาที่โหลดงานตัวแรกของสไตล์ปัจจุบัน  ",type="datetime",variable=self.var_CurrentStyleStartDate)
        self.CurrentStyleStartDate.pack(side='top',padx=3,pady=3)

        self.var_CurrentStyleCompleteDate = DateTimeVar(detect_changes=True)
        self.CurrentStyleCompleteDate = LinearDateSelector(self.frame_EventTimes,frame_title="  วัน/เวลาที่ตรวจงานตัวแรกของสไตล์ปัจจุบัน  ",type="datetime",variable=self.var_CurrentStyleCompleteDate)
        self.CurrentStyleCompleteDate.pack(side='top',padx=3,pady=3)

        self.labelframe_Defaults = ttk.LabelFrame(self.frame_EventTimes, text="ค่าเริ่มต้น")
        self.labelframe_Defaults.pack(side='top',padx=3,pady=3, fill='x')
        self.margin_Defaults = ttk.Frame(self.labelframe_Defaults)
        self.margin_Defaults.pack(side='top',padx=2,pady=2, fill='both')

        ttk.Label(self.margin_Defaults, text="เวลาเริ่มงาน", justify='left').grid(row=0,column=0,padx=3,pady=3,sticky='nsew')
        ttk.Label(self.margin_Defaults, text="เวลาพักกลางวัน", justify='left').grid(row=1,column=0,padx=3,pady=3,sticky='nsew')
        ttk.Label(self.margin_Defaults, text="เวลาเริ่มงานตอนบ่าย", justify='left').grid(row=2,column=0,padx=3,pady=3,sticky='nsew')
        ttk.Label(self.margin_Defaults, text="เวลาเลิกงาน", justify='left').grid(row=3,column=0,padx=3,pady=3,sticky='nsew')
        
        ttk.Spinbox(self.margin_Defaults, textvariable=self.default_MorningShiftBegins, values=tuple_spinner_morning, width=10).grid(row=0,column=1,padx=3,pady=3,sticky='nsew')
        ttk.Spinbox(self.margin_Defaults, textvariable=self.default_MorningShiftEnds, values=tuple_spinner_afternoon, width=10).grid(row=1,column=1,padx=3,pady=3,sticky='nsew')
        ttk.Spinbox(self.margin_Defaults, textvariable=self.default_AfternoonBegins, values=tuple_spinner_afternoon, width=10).grid(row=2,column=1,padx=3,pady=3,sticky='nsew')
        ttk.Spinbox(self.margin_Defaults, textvariable=self.default_AfternoonEnds, values=tuple_spinner_evening, width=10).grid(row=3,column=1,padx=3,pady=3,sticky='nsew')

        ttk.Button(self.margin_Defaults, text="รีเซ็ตเวลาเริ่มงาน",width=15).grid(row=0,column=2,padx=3,pady=3,sticky='nsew')
        ttk.Button(self.margin_Defaults, text="รีเซ็ตเวลาพักกลางวัน", width=15).grid(row=1,column=2,padx=3,pady=3,sticky='nsew')
        ttk.Button(self.margin_Defaults, text="รีเซ็ตเวลาเริ่มงานตอนบ่าย", width=15).grid(row=2,column=2,padx=3,pady=3,sticky='nsew')
        ttk.Button(self.margin_Defaults, text="รีเซ็ตเวลาเลิกงาน", width=15).grid(row=3,column=2,padx=3,pady=3,sticky='nsew')


        self.frame_CalculatorControl = ttk.LabelFrame(self.frame_Calculation,text=" ตัวควบคุมเครื่องมือคำนวณ ")
        self.frame_CalculatorControl.pack(side='top',fill='x',padx=5,pady=5)

        self.btn_CalcCtrl_CreateTimeline = ttk.Button(self.frame_CalculatorControl, text="สร้างเส้นเวลา",style='TButton', width=30, command=lambda:self.getSelectedDate())
        self.btn_CalcCtrl_CreateTimeline.pack(side='left',padx=5,pady=5)
        self.btn_CalcCtrl_ExecuteCalculate = ttk.Button(self.frame_CalculatorControl, text="คำนวณเวลาเดี๋ยวนี้",style='success.TButton', width=30, command=lambda:self.Calculate())
        self.btn_CalcCtrl_ExecuteCalculate.pack(side='left',padx=5,pady=5)
        self.btn_CalcCtrl_ResetCalc = ttk.Button(self.frame_CalculatorControl, text="รีเซ็ตตารางคำนวณ", style='outline.TButton',width=20)
        self.btn_CalcCtrl_ResetCalc.pack(side='right',padx=5,pady=5)
        self.btn_CalcCtrl_ResetOvertime = ttk.Button(self.frame_CalculatorControl, text="รีเซ็ตเฉพาะเวลาโอที", style='outline.TButton',width=20)
        self.btn_CalcCtrl_ResetOvertime.pack(side='right',padx=5,pady=5)



        self.labelframe_CalculationTable = ttk.LabelFrame(self.frame_Calculation,text=" ตารางคำนวณ ")
        self.labelframe_CalculationTable.pack(side='top',fill='x',padx=5,pady=5)
        self.margin_CalculationTable = ttk.Frame(self.labelframe_CalculationTable)
        self.margin_CalculationTable.pack(side='top',fill='both',padx=5,pady=5)

        self.frame_defaults = ttk.Frame(self.margin_CalculationTable)
        #self.frame_defaults.pack(side='left',fill='y')
        self.frame_datatable = ttk.Frame(self.margin_CalculationTable)
        #self.frame_datatable.pack(side='left',fill='both',expand=True)
        self.canvas_CalculationTable = tk.Canvas(self.frame_datatable,height=370)
        self.canvas_CalculationTable.pack(side='top',fill="both",expand=True)
        
        self.frame_CalculationTable = ttk.Frame(self.canvas_CalculationTable)
        self.frame_CalculationTable.bind("<Configure>",lambda e: self.canvas_CalculationTable.configure(scrollregion=self.canvas_CalculationTable.bbox("all")))
        self.canvas_CalculationTable.create_window((0,0),anchor='nw',window=self.frame_CalculationTable)

        self.ExplorerBacklogData_hscrollCanvas = ttk.Scrollbar(self.frame_datatable,orient='horizontal',command=self.canvas_CalculationTable.xview)
        self.ExplorerBacklogData_hscrollCanvas.pack(side='top',fill='x')
        self.canvas_CalculationTable.configure(xscrollcommand=self.ExplorerBacklogData_hscrollCanvas.set)

        

        ttk.Label(self.frame_defaults, text="ค่าเริ่มต้น").grid(row=0,column=0,columnspan=2,padx=0,pady=0)

        ttk.Spinbox(self.frame_defaults, textvariable=self.default_MorningShiftBegins, width=5, values=tuple_spinner_morning).grid(row=4,column=0)
        ttk.Spinbox(self.frame_defaults, textvariable=self.default_MorningShiftEnds, width=5, values=tuple_spinner_afternoon).grid(row=5,column=0)
        ttk.Spinbox(self.frame_defaults, textvariable=self.default_AfternoonBegins, width=5, values=tuple_spinner_afternoon).grid(row=6,column=0)
        ttk.Spinbox(self.frame_defaults, textvariable=self.default_AfternoonEnds, width=5, values=tuple_spinner_evening).grid(row=7,column=0)
        
        ttk.Button(self.frame_defaults, text='',state='disabled').grid(row=1,column=1,padx=0,pady=0)
        ttk.Button(self.frame_defaults, text='',state='disabled').grid(row=2,column=1,padx=0,pady=0)
        ttk.Button(self.frame_defaults, text='รีเซ็ต').grid(row=3,column=1,padx=0,pady=0)
        ttk.Button(self.frame_defaults, text='รีเซ็ต').grid(row=4,column=1,padx=0,pady=0)
        ttk.Button(self.frame_defaults, text='รีเซ็ต').grid(row=5,column=1,padx=0,pady=0)
        ttk.Button(self.frame_defaults, text='รีเซ็ต').grid(row=6,column=1,padx=0,pady=0)
        ttk.Button(self.frame_defaults, text='รีเซ็ต').grid(row=7,column=1,padx=0,pady=0)
        ttk.Button(self.frame_defaults, text='รีเซ็ต').grid(row=8,column=1,padx=0,pady=0)
        ttk.Button(self.frame_defaults, text='รีเซ็ต').grid(row=9,column=1,padx=0,pady=0)
        ttk.Button(self.frame_defaults, text='รีเซ็ต').grid(row=10,column=1,padx=0,pady=0)
        ttk.Button(self.frame_defaults, text='',state='disabled').grid(row=11,column=1,padx=0,pady=0)
        ttk.Button(self.frame_defaults, text='',state='disabled').grid(row=12,column=1,padx=0,pady=0)

        ttk.Label(self.margin_CalculationTable, text='วันที่', justify='right').grid(row=1,column=2,padx=0,pady=0,sticky='nsew')
        ttk.Label(self.margin_CalculationTable, text='วันในสัปดาห์', justify='right').grid(row=2,column=2,padx=0,pady=0,sticky='nsew')
        ttk.Label(self.margin_CalculationTable, text='เป็นวันหยุดหรือไม่?', justify='right').grid(row=3,column=2,padx=0,pady=0,sticky='nsew')
        ttk.Label(self.margin_CalculationTable, text='เวลาเริ่มงาน', justify='right').grid(row=4,column=2,padx=0,pady=0,sticky='nsew')
        ttk.Label(self.margin_CalculationTable, text='พักกลางวัน', justify='right').grid(row=5,column=2,padx=0,pady=0,sticky='nsew')
        ttk.Label(self.margin_CalculationTable, text='เรื่มงานบ่าย', justify='right').grid(row=6,column=2,padx=0,pady=0,sticky='nsew')
        ttk.Label(self.margin_CalculationTable, text='เลิกงาน', justify='right').grid(row=7,column=2,padx=0,pady=0,sticky='nsew')
        ttk.Label(self.margin_CalculationTable, text='เริ่มโอที', justify='right').grid(row=8,column=2,padx=0,pady=0,sticky='nsew')
        ttk.Label(self.margin_CalculationTable, text='เลิกโอที', justify='right').grid(row=9,column=2,padx=0,pady=0,sticky='nsew')
        ttk.Label(self.margin_CalculationTable, text='หักเวลาพิเศษ', justify='right').grid(row=10,column=2,padx=0,pady=0,sticky='nsew')
        ttk.Label(self.margin_CalculationTable, text='Throughput Time', justify='right').grid(row=11,column=2,padx=0,pady=0,sticky='nsew')
        ttk.Label(self.margin_CalculationTable, text='Changeover Time', justify='right').grid(row=12,column=2,padx=0,pady=0,sticky='nsew')
        for d in range(1,15):
            self.array_CalculationDates.append(LocalChangeoverDate(self.margin_CalculationTable,column=d,offset=3))


        self.labelframe_Results = ttk.LabelFrame(self.frame_Calculation,text=" ผลการคำนวณ ")
        self.labelframe_Results.pack(side='top',fill='x',padx=5,pady=5)
        self.frame_Results = ttk.Frame(self.labelframe_Results)
        self.frame_Results.pack(side='top',fill='x',padx=5,pady=5)

        self.fframe_TotalThroughputTime = ttk.Frame(self.frame_Results)
        self.fframe_TotalThroughputTime.pack(side='left',padx=5)
        self.fframe_TotalChangeoverTime = ttk.Frame(self.frame_Results)
        self.fframe_TotalChangeoverTime.pack(side='left',padx=5)

        ttk.Label(self.fframe_TotalChangeoverTime,text="Changeover Time:").pack(side='top')
        ttk.Entry(self.fframe_TotalChangeoverTime,textvariable=self.total_ChangeoverTime).pack(side='top')
        ttk.Label(self.fframe_TotalThroughputTime,text="Throughput Time:").pack(side='top')
        ttk.Entry(self.fframe_TotalThroughputTime,textvariable=self.total_ThroughputTime).pack(side='top')


    def getSelectedDate(self):
        self.btn_CalcCtrl_CreateTimeline.configure(text="อัพเดตเส้นเวลา")
        self.LastEnd = self.var_PreviousStyleEndDate.get_datetime()
        self.FirstStart = self.var_CurrentStyleStartDate.get_datetime()
        self.FirstEnd = self.var_CurrentStyleCompleteDate.get_datetime()

        if self.FirstStart > self.FirstEnd:
            messagebox.showwarning("ไม่ถูกต้อง","วันที่และเวลาที่เริ่มงานสไตล์ใหม่จะต้องเกิดขึ้นก่อนวันที่และเวลาที่ตรวจงานตัวแรกของสไตล์ใหม่")
            return
        else:
            TimelineStartDate = min(self.LastEnd,self.FirstStart,self.FirstEnd).date()
            TimelineEndDate = max(self.LastEnd,self.FirstStart,self.FirstEnd).date()
            
            for col in range(0,14):
                print(f"col= {col}, Start = {TimelineStartDate.__add__(timedelta(col))}, End = {TimelineEndDate}")
                self.array_CalculationDates[col].Date.set('')
                self.array_CalculationDates[col].DayofWeek.set('')
                if TimelineStartDate.__add__(timedelta(col)) > TimelineEndDate:
                    self.array_CalculationDates[col].ctrl_Date.configure(state='disabled')
                    self.array_CalculationDates[col].ctrl_DayOfWeek.configure(state='disabled')
                    self.array_CalculationDates[col].ctrl_IsHoliday.configure(state='disabled')
                    self.array_CalculationDates[col].ctrl_MorningBegins.configure(state='disabled')
                    self.array_CalculationDates[col].ctrl_MorningEnds.configure(state='disabled')
                    self.array_CalculationDates[col].ctrl_AfternoonBegins.configure(state='disabled')
                    self.array_CalculationDates[col].ctrl_AfternoonEnds.configure(state='disabled')
                    self.array_CalculationDates[col].ctrl_OvertimeBegins.configure(state='disabled')
                    self.array_CalculationDates[col].ctrl_OvertimeEnds.configure(state='disabled')
                    self.array_CalculationDates[col].ctrl_ExcludedTime.configure(state='disabled')
                    self.array_CalculationDates[col].ctrl_LocalThroughput.configure(state='disabled')
                    self.array_CalculationDates[col].ctrl_LocalChangeover.configure(state='disabled')
                    
                else:
                    self.array_CalculationDates[col].ctrl_Date.configure(state='normal')
                    self.array_CalculationDates[col].ctrl_DayOfWeek.configure(state='normal')
                    self.array_CalculationDates[col].ctrl_IsHoliday.configure(state='normal')
                    self.array_CalculationDates[col].ctrl_MorningBegins.configure(state='normal')
                    self.array_CalculationDates[col].ctrl_MorningEnds.configure(state='normal')
                    self.array_CalculationDates[col].ctrl_AfternoonBegins.configure(state='normal')
                    self.array_CalculationDates[col].ctrl_AfternoonEnds.configure(state='normal')
                    self.array_CalculationDates[col].ctrl_OvertimeBegins.configure(state='normal')
                    self.array_CalculationDates[col].ctrl_OvertimeEnds.configure(state='normal')
                    self.array_CalculationDates[col].ctrl_ExcludedTime.configure(state='normal')
                    self.array_CalculationDates[col].ctrl_LocalThroughput.configure(state='normal')
                    self.array_CalculationDates[col].ctrl_LocalChangeover.configure(state='normal')

                    self.array_CalculationDates[col].Date.set(str(TimelineStartDate.__add__(timedelta(days=col)).strftime("%d-%m-%y")))
                    self.array_CalculationDates[col].DayofWeek.set(str(TimelineStartDate.__add__(timedelta(days=col)).strftime("%a")))
                    if TimelineStartDate.__add__(timedelta(days=col)).weekday() == 6:
                        self.array_CalculationDates[col].IsHoliday.set(True)
                        self.array_CalculationDates[col].setHolidayFieldLock()
                    if col == 0 or TimelineStartDate.__add__(timedelta(days=col)) == TimelineEndDate:
                        # If the column being created is either first or last column, lock the IsHoliday Checkbutton so these columns cannot be set to holiday.
                        self.array_CalculationDates[col].ctrl_IsHoliday.configure(state='disabled')
    def Calculate(self):
        tag_Changeover_Begin = False
        tag_Throughput_Begin = False
        tag_Changeover_End = False
        tag_Throughput_End = False

        self.LastEnd = self.var_PreviousStyleEndDate.get_datetime()
        self.FirstStart = self.var_CurrentStyleStartDate.get_datetime()
        self.FirstEnd = self.var_CurrentStyleCompleteDate.get_datetime()
        TP_begin = self.FirstStart
        TP_end = self.FirstEnd
        oldend = self.LastEnd
        newend = self.FirstEnd
        CH_begin = min(oldend,newend)
        CH_end = max(oldend,newend)

        tCH = 0
        tTP = 0


        for col in range(0,14):
            #===== อ่านเวลาจากแต่ละคอลัมน์... ===========================================================
            try:
                dt = self.array_CalculationDates[col].Date.get().split('-')
                useable_timeline_date = date(2000+int(dt[2]),int(dt[1]),int(dt[0]))
            except (IndexError, ValueError):
                break

            morningBegins = time(int(self.array_CalculationDates[col].MorningShiftBegins.get().split('.')[0]),int(self.array_CalculationDates[col].MorningShiftBegins.get().split('.')[1],0))
            lunchBegins = time(int(self.array_CalculationDates[col].MorningShiftEnds.get().split('.')[0]),int(self.array_CalculationDates[col].MorningShiftEnds.get().split('.')[1],0))
            afternoonBegins = time(int(self.array_CalculationDates[col].AfternoonBegins.get().split('.')[0]),int(self.array_CalculationDates[col].AfternoonBegins.get().split('.')[1],0))
            eveningEnds = time(int(self.array_CalculationDates[col].ShiftEnds.get().split('.')[0]),int(self.array_CalculationDates[col].ShiftEnds.get().split('.')[1],0))
            try:
                overtimeBegins = time(int(self.array_CalculationDates[col].OvertimeBegins.get().split('.')[0]),int(self.array_CalculationDates[col].OvertimeBegins.get().split('.')[1],0))
                overtimeEnds = time(int(self.array_CalculationDates[col].OvertimeEnds.get().split('.')[0]),int(self.array_CalculationDates[col].OvertimeEnds.get().split('.')[1],0))
            except ValueError:
                overtimeBegins = 'X'
                overtimeEnds = 'X'
            deduction = self.array_CalculationDates[col].ExcludedTime.get()
            
            #===== CHECK THROUGHPUT... ===========================================================
            if useable_timeline_date >= self.LastEnd.date() and useable_timeline_date <= TP_end.date(): #เริ่มเช็คเมื่อวันที่บนหัวคอลัมน์ อยู่ระหว่างวันเริ่มและวันสิ้นสุด TP...
                if not tag_Throughput_Begin: # ถ้าถึงช่วง TP ครั้งแรก... ให้เช็คก่อนว่าตกขอบหรือไม่
                    if TP_begin.time() < morningBegins:
                        messagebox.showwarning(title="คำเตือน", message=f"เวลาที่โหลดงานใหม่ไม่สามารถเกิดขึ้นก่อนเวลาเริ่มงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                        return
                    if TP_begin.time() >= lunchBegins and TP_begin.time() < afternoonBegins:
                        messagebox.showwarning(title="คำเตือน", message=f"เวลาที่โหลดงานใหม่ไม่สามารถเกิดขึ้นระหว่างช่วงพักกลางวัน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                        return
                    if overtimeBegins == 'X':
                        if TP_begin.time() >= eveningEnds:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่โหลดงานใหม่ไม่สามารถเกิดขึ้นหลังเลิกงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return
                    if overtimeBegins != 'X':
                        if TP_begin.time() >= eveningEnds and TP_begin.time() < overtimeBegins:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่โหลดงานใหม่ไม่สามารถเกิดขึ้นในช่วงพักล่วงเวลา\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return
                        elif TP_begin.time() >= overtimeEnds:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่โหลดงานใหม่ไม่สามารถเกิดขึ้นหลังเลิกงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return
                    
                    if TP_end.time() < morningBegins:
                        messagebox.showwarning(title="คำเตือน", message=f"เวลาที่ตรวจผ่านงานใหม่ไม่สามารถเกิดขึ้นก่อนเวลาเริ่มงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                        return
                    if TP_end.time() >= lunchBegins and TP_end.time() < afternoonBegins:
                        messagebox.showwarning(title="คำเตือน", message=f"เวลาที่ตรวจผ่านงานใหม่ไม่สามารถเกิดขึ้นระหว่างช่วงพักกลางวัน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                        return
                    if overtimeBegins == 'X':
                        if TP_end.time() >= eveningEnds:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่ตรวจผ่านงานใหม่ไม่สามารถเกิดขึ้นหลังเลิกงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return
                    if overtimeBegins != 'X':
                        if TP_end.time() >= eveningEnds and TP_end.time() < overtimeBegins:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่ตรวจผ่านงานใหม่ไม่สามารถเกิดขึ้นในช่วงพักล่วงเวลา\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return
                        elif TP_end.time() >= overtimeEnds:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่ตรวจผ่านงานใหม่ไม่สามารถเกิดขึ้นหลังเลิกงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return

                    if TP_begin.date() == TP_end.date(): # กรณี TP เริ่มและจบวันเดียวกัน จะเช็คว่าเริ่มและจบในกรอบเวลาเดียวกันหรือไม่ แล้วคำนวณเวลาออกมา
                        tag_Throughput_Begin = True
                        tag_Throughput_End = True
                        # เช้า - เช้า
                        if TP_begin.time() < lunchBegins and TP_end.time() < lunchBegins:
                            TP = pyra.convertTimeToDuration(TP_begin.time(), TP_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        # เช้า - บ่าย
                        elif TP_begin.time() < lunchBegins and TP_end.time() >= afternoonBegins and TP_end.time() < eveningEnds:
                            TP = pyra.convertTimeToDuration(TP_begin.time(), lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, TP_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        # เช้า - โอที
                        elif TP_begin.time() < lunchBegins and TP_end.time() >= overtimeBegins and overtimeBegins != 'X':
                            TP = pyra.convertTimeToDuration(TP_begin.time(), lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, eveningEnds,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(overtimeBegins, TP_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        # บ่าย - บ่าย
                        elif TP_begin.time() < eveningEnds and TP_end.time() < eveningEnds:
                            TP = pyra.convertTimeToDuration(TP_begin.time(), TP_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        # บ่าย - โอที
                        elif TP_begin.time() < eveningEnds and TP_end.time() >= overtimeBegins and overtimeBegins != 'X':
                            TP = pyra.convertTimeToDuration(TP_begin.time(), eveningEnds,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(overtimeBegins, TP_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        # โอที - บ่าย
                        elif TP_begin.time() < overtimeEnds and TP_end.time() < overtimeEnds and overtimeBegins != 'X':
                            TP = pyra.convertTimeToDuration(TP_begin.time(), TP_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                    else: # แต่ถ้า TP เริ่มและจบคนละวัน จะคำนวณเฉพาะเวลาเริ่มต้น ไปจนสุดเวลาเลิกงาน
                        tag_Throughput_Begin = True
                        if TP_begin.time() < lunchBegins:
                            TP = pyra.convertTimeToDuration(TP_begin.time(), lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, eveningEnds,output_unit="minutes", rounding_mode='away_from_zero')+(pyra.convertTimeToDuration(overtimeBegins, overtimeEnds,output_unit="minutes", rounding_mode='away_from_zero') if overtimeBegins != 'X' else 0)-deduction
                        elif TP_begin.time() < eveningEnds:
                            TP = pyra.convertTimeToDuration(TP_begin.time(), eveningEnds,output_unit="minutes", rounding_mode='away_from_zero')+(pyra.convertTimeToDuration(overtimeBegins, overtimeEnds,output_unit="minutes", rounding_mode='away_from_zero') if overtimeBegins != 'X' else 0)-deduction
                        elif TP_begin.time() < overtimeEnds and overtimeBegins != 'X':
                            TP = pyra.convertTimeToDuration(TP_begin.time(), overtimeEnds,output_unit="minutes", rounding_mode='away_from_zero')-deduction
                elif tag_Throughput_Begin == True and tag_Throughput_End == False: # ถ้าคำนวณเวลาเริ่ม TP ไปแล้ว จะเช็คต่อไปว่าเวลาจบ TP ยังค้างอยู่หรือไม่ แล้วจะเช็คว่าถ้าวันนี้ยังไม่ใช่ TP จะคำนวณเวลาทำงานเต็มวัน
                    if TP_end.date() == useable_timeline_date:
                        tag_Throughput_End = True
                        # เช้า - เช้า
                        if TP_end.time() < lunchBegins:
                            TP = pyra.convertTimeToDuration(morningBegins, TP_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        elif TP_end.time() < eveningEnds:
                            TP = pyra.convertTimeToDuration(morningBegins, lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, TP_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        elif TP_end.time() < overtimeEnds and overtimeBegins != 'X':
                            TP = pyra.convertTimeToDuration(morningBegins, lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, eveningEnds,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(overtimeBegins, TP_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                    else:
                        TP = pyra.convertTimeToDuration(morningBegins, lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, eveningEnds,output_unit="minutes", rounding_mode='away_from_zero')+(pyra.convertTimeToDuration(overtimeBegins, overtimeEnds,output_unit="minutes", rounding_mode='away_from_zero') if overtimeBegins != 'X' else 0)-deduction
                else:
                    TP = 0
            else:
                TP = 0
            tTP += TP
            self.array_CalculationDates[col].LocalThroughputTime.set(TP)
            
            #===== CHECK CHANGEOVER... ===========================================================

            if useable_timeline_date >= CH_begin.date() and useable_timeline_date <= CH_end.date(): #เริ่มเช็คเมื่อวันที่บนหัวคอลัมน์ อยู่ระหว่างวันเริ่มและวันสิ้นสุด CH...
                if not tag_Changeover_Begin: # ถ้าถึงช่วง CH ครั้งแรก... ให้เช็คก่อนว่าตกขอบหรือไม่
                    if CH_begin.time() < morningBegins:
                        messagebox.showwarning(title="คำเตือน", message=f"เวลาที่โหลดงานใหม่ไม่สามารถเกิดขึ้นก่อนเวลาเริ่มงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                        return
                    if CH_begin.time() >= lunchBegins and CH_begin.time() < afternoonBegins:
                        messagebox.showwarning(title="คำเตือน", message=f"เวลาที่โหลดงานใหม่ไม่สามารถเกิดขึ้นระหว่างช่วงพักกลางวัน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                        return
                    if overtimeBegins == 'X':
                        if CH_begin.time() >= eveningEnds:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่โหลดงานใหม่ไม่สามารถเกิดขึ้นหลังเลิกงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return
                    if overtimeBegins != 'X':
                        if CH_begin.time() >= eveningEnds and CH_begin.time() < overtimeBegins:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่โหลดงานใหม่ไม่สามารถเกิดขึ้นในช่วงพักล่วงเวลา\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return
                        elif CH_begin.time() >= overtimeEnds:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่โหลดงานใหม่ไม่สามารถเกิดขึ้นหลังเลิกงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return
                    
                    if CH_end.time() < morningBegins:
                        messagebox.showwarning(title="คำเตือน", message=f"เวลาที่ตรวจผ่านงานใหม่ไม่สามารถเกิดขึ้นก่อนเวลาเริ่มงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                        return
                    if CH_end.time() >= lunchBegins and CH_end.time() < afternoonBegins:
                        messagebox.showwarning(title="คำเตือน", message=f"เวลาที่ตรวจผ่านงานใหม่ไม่สามารถเกิดขึ้นระหว่างช่วงพักกลางวัน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                        return
                    if overtimeBegins == 'X':
                        if CH_end.time() >= eveningEnds:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่ตรวจผ่านงานใหม่ไม่สามารถเกิดขึ้นหลังเลิกงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return
                    if overtimeBegins != 'X':
                        if CH_end.time() >= eveningEnds and CH_end.time() < overtimeBegins:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่ตรวจผ่านงานใหม่ไม่สามารถเกิดขึ้นในช่วงพักล่วงเวลา\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return
                        elif CH_end.time() >= overtimeEnds:
                            messagebox.showwarning(title="คำเตือน", message=f"เวลาที่ตรวจผ่านงานใหม่ไม่สามารถเกิดขึ้นหลังเลิกงาน\n\nตำแหน่งคอลัมน์วันที่ {useable_timeline_date}")
                            return

                    if CH_begin.date() == CH_end.date(): # กรณี CH เริ่มและจบวันเดียวกัน จะเช็คว่าเริ่มและจบในกรอบเวลาเดียวกันหรือไม่ แล้วคำนวณเวลาออกมา
                        tag_Changeover_Begin = True
                        tag_Changeover_End = True
                        # เช้า - เช้า
                        if CH_begin.time() < lunchBegins and CH_end.time() < lunchBegins:
                            CH = pyra.convertTimeToDuration(CH_begin.time(), CH_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        # เช้า - บ่าย
                        elif CH_begin.time() < lunchBegins and CH_end.time() >= afternoonBegins and CH_end.time() < eveningEnds:
                            CH = pyra.convertTimeToDuration(CH_begin.time(), lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, CH_end.time(),output_unit="minutes")-deduction
                        # เช้า - โอที
                        elif CH_begin.time() < lunchBegins and CH_end.time() >= overtimeBegins and overtimeBegins != 'X':
                            CH = pyra.convertTimeToDuration(CH_begin.time(), lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, eveningEnds,output_unit="minutes")+pyra.convertTimeToDuration(overtimeBegins, CH_end.time(),output_unit="minutes")-deduction
                        # บ่าย - บ่าย
                        elif CH_begin.time() < eveningEnds and CH_end.time() < eveningEnds:
                            CH = pyra.convertTimeToDuration(CH_begin.time(), CH_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        # บ่าย - โอที
                        elif CH_begin.time() < eveningEnds and CH_end.time() >= overtimeBegins and overtimeBegins != 'X':
                            CH = pyra.convertTimeToDuration(CH_begin.time(), eveningEnds,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(overtimeBegins, CH_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        # โอที - บ่าย
                        elif CH_begin.time() < overtimeEnds and CH_end.time() < overtimeEnds and overtimeBegins != 'X':
                            CH = pyra.convertTimeToDuration(CH_begin.time(), CH_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                    else: # แต่ถ้า CH เริ่มและจบคนละวัน จะคำนวณเฉพาะเวลาเริ่มต้น ไปจนสุดเวลาเลิกงาน
                        tag_Changeover_Begin = True
                        if CH_begin.time() < lunchBegins:
                            CH = pyra.convertTimeToDuration(CH_begin.time(), lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, eveningEnds,output_unit="minutes", rounding_mode='away_from_zero')+(pyra.convertTimeToDuration(overtimeBegins, overtimeEnds,output_unit="minutes", rounding_mode='away_from_zero') if overtimeBegins != 'X' else 0)-deduction
                        elif CH_begin.time() < eveningEnds:
                            CH = pyra.convertTimeToDuration(CH_begin.time(), eveningEnds,output_unit="minutes", rounding_mode='away_from_zero')+(pyra.convertTimeToDuration(overtimeBegins, overtimeEnds,output_unit="minutes", rounding_mode='away_from_zero') if overtimeBegins != 'X' else 0)-deduction
                        elif CH_begin.time() < overtimeEnds and overtimeBegins != 'X':
                            CH = pyra.convertTimeToDuration(CH_begin.time(), overtimeEnds,output_unit="minutes", rounding_mode='away_from_zero')-deduction
                elif tag_Changeover_Begin == True and tag_Changeover_End == False: # ถ้าคำนวณเวลาเริ่ม CH ไปแล้ว จะเช็คต่อไปว่าเวลาจบ CH ยังค้างอยู่หรือไม่ แล้วจะเช็คว่าถ้าวันนี้ยังไม่ใช่ CH จะคำนวณเวลาทำงานเต็มวัน
                    if CH_end.date() == useable_timeline_date:
                        tag_Changeover_End = True
                        # เช้า - เช้า
                        if CH_end.time() < lunchBegins:
                            CH = pyra.convertTimeToDuration(morningBegins, CH_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        elif CH_end.time() < eveningEnds:
                            CH = pyra.convertTimeToDuration(morningBegins, lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, CH_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                        elif CH_end.time() < overtimeEnds and overtimeBegins != 'X':
                            CH = pyra.convertTimeToDuration(morningBegins, lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, eveningEnds,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(overtimeBegins, CH_end.time(),output_unit="minutes", rounding_mode='away_from_zero')-deduction
                    else:
                        CH = pyra.convertTimeToDuration(morningBegins, lunchBegins,output_unit="minutes", rounding_mode='away_from_zero')+pyra.convertTimeToDuration(afternoonBegins, eveningEnds,output_unit="minutes", rounding_mode='away_from_zero')+(pyra.convertTimeToDuration(overtimeBegins, overtimeEnds,output_unit="minutes", rounding_mode='away_from_zero') if overtimeBegins != 'X' else 0)-deduction
                else:
                    CH = 0
            else:
                CH = 0
            tCH += CH
            self.array_CalculationDates[col].LocalChangeoverTime.set(CH)
            print(f"Column Number {col}")
            print(useable_timeline_date)
            print(f"CH = {CH}, TP = {TP}")
            print("-----")

    def resetTime(self,time_mode:str):
        pass




if __name__ == "__main__":
    rt = Style.master
    #rt = tk.Tk()
    windowRoot = App(rt,title="Changeover Time Calculator")
    rt.mainloop()