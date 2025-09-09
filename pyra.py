"""ฟังก์ชันสุ่มๆ ที่ช่วยให้การทำงานกับวันที่และเวลาง่ายขึ้น\n\nสร้างโดย Sutthinan D."""

from datetime import datetime, date, time, timedelta
import math

# ====================================================================================
# =====  CONTENTS  ===================================================================
# ====================================================================================
# =====  1. Timestamp
'''createDisplayTimestamp'''
# สร้างสตริงที่ประกอบจากวันที่และเวลาปัจจุบันจากการกำหนดรูปแบบวันที่และเวลามาตรฐาน
'''createDataTimestamp'''
# สร้างสตริงประทับเวลามาตรฐานในรูปแบบ yyyymmdd-hhmmss จากวันที่และเวลาปัจจุบัน

# =====  2. Date and Time Formatting
'''ReformatDate'''
# แปลงค่าประเภทวันที่ (ได้ทั้งชนิดข้อมูล datetime.date และ datetime.datetime) ให้เป็นรูปแบบมาตรฐานที่อ่านได้ง่าย
# ฟังก์ชันนี้เป็นฟังก์ชัน createDisplayTimestamp ชนิดที่ใช้กับค่าวันที่และเวลาที่มีอยู่แล้ว
'''decodeDataTimestamp'''
# แปลงการจัดรูปแบบวันที่ เวลา หรือวันที่และเวลาที่อยู่ในรูปแบบประทับเวลาข้อมูลมาตรฐาน "yyyymmdd-hhmmss" ให้เป็นวันที่ในรูปแบบที่อ่านได้
'''encodeDataTimestamp'''
# แปลงค่าประเภทวันที่ (ได้ทั้งชนิดข้อมูล datetime.date และ datetime.datetime) ให้เป็นรูปแบบประทับเวลาข้อมูลมาตรฐาน "yyyymmdd-hhmmss"
# ฟังก์ชันนี้เป็นฟังก์ชัน createDataTimestamp ชนิดที่ใช้กับค่าวันที่และเวลาที่มีอยู่แล้ว

# =====  3. Date and Time Parts
'''getWeekday'''
# คืนค่าสตริงที่ระบุวันที่ในสัปดาห์ จากข้อมูลวันที่แบบ datetime.date หรือ datetime.datetime ที่ได้รับเข้ามา
'''getMillseconds'''
# คืนจำนวนเต็มหรือตัวเลขมีทศนิยมที่เท่ากับเศษของวินาที (ในหน่วยมิลลิวินาที) ของเวลาปัจจุบัน (สามารถเลือกคืนเศษมิลลิวินาทีในวินาทีเดียวกัน )
'''convertWord'''
# คืนดัชนีจำนวนเต็ม ที่ได้จากการเทียบค่าที่รับเข้ามาซึ่งเป็นสตริงแทนวันที่ในสัปดาห์หรือเดือน
'''netWorkMinutes'''
'''getDailyWorkMinutes'''
# NOTE รับ datetime.date หรือ datetime.datetime แล้วตรวจสอบว่า ถ้าเป็นวันอาทิตย์ หรือตรงกับวันที่ที่ระบุใน iterable วันหยุด ให้ข้าม แล้วคืน 0
# จากนั้น จะดูว่า กำหมดมาว่าทำโอทีกี่นาที แล้วเพิ่มเวลาทำงาน แล้วคืนเป็นจำนวนนาที

# ===== 4. ระบบคำนวณเวลาทำงาน
'''คลาส WorkMinutes'''
# ลิสต์สองมิติที่ประกอบด้วยวันที่แบบ datetime.date, ค่าชั่วโมงและนาทีแบบ datetime.timedelta และชนิดวันที่

'''init จะรับ datetime.datetime สองค่า แล้วคำนวณ WorkMinutes ออกมาเป็น object WorkMinutes'''

''''''

'''getWorkMinuteHead'''
# รับเวลาการทำงาน และ datetime.datetime หรือ datetime.time 


# ====================================================================================
# =====  CONTENTS  ===================================================================
# ====================================================================================

TH_Full_Weekdays = ("วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์")
TH_Abbreviated_Weekdays = ("อา.", "จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส.")
TH_Full_Months = ("มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม")
TH_Abbreviated_Months = ("ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ย.", "ส.ค", "ก.ค", "ต.ค.", "พ.ย.", "ธ.ค.")

EN_Full_Weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
EN_Abbreviated_Weekdays = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
EN_Symbol_Weekdays = ("S", "M", "T", "W", "T", "F", "S")
EN_Full_Months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
EN_Abbreviated_Months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

def createDisplayTimestamp(date_and_time=datetime.now(), date_format_type='short', time_format_type='off', locale='TH', yearsystem='AD', date_delimiter='/', time_delimiter=':', leading_zeroes=False):
    """สร้างสตริงที่ประกอบจากวันที่และเวลาปัจจุบันจากการกำหนดรูปแบบวันที่และเวลามาตรฐาน"""
    #region ===== FULL EXAMPLE GUIDE =====
    # UNIVERSAL PARAMETERS as follows: yearsystem='AD', date_delimiter='/', time_delimiter=':'
    #--------------------------------------------------------------------------------------------------------------------------------------
    #                   locale='TH'                 locale='TH'                 locale='EN'                 locale='EN'
    # DATE FORMATS      leading_zeroes=False        leading_zeroes=True         leading_zeroes=False        leading_zeroes=True
    #--------------------------------------------------------------------------------------------------------------------------------------
    # SHORT             5/7/24                      05/07/24                    5/7/24                      05/07/24
    # MEDIUM            5/7/2024                    05/07/2024                  5/7/2024                    05/07/2024
    # ABBR              5 ก.ค. 2024                 05 ก.ค. 2024                5 Jul 2024                  05 Jul 2024
    # LONG              5 กรกฎาคม 2024              05 กรกฎาคม 2024             5 July 2024                 05 July 2024
    # FULL              วันศุกร์ที่ 5 กรกฎาคม 2024       วันศุกร์ที่ 05 กรกฎาคม 2024      Friday, 5 July, 2024        Friday, 05 July, 2024
    # DATA_SHORT        240705                      240705                      240705                      240705 
    # DATA_LONG         20240705                    20240705                    20240705                    20240705
    # OFF               /date disabled/

    #--------------------------------------------------------------------------------------------------------------------------------------
    #                   locale='TH'                 locale='TH'                 locale='EN'                 locale='EN'
    # TIME FORMATS      leading_zeroes=False        leading_zeroes=True         leading_zeroes=False        leading_zeroes=True
    #--------------------------------------------------------------------------------------------------------------------------------------
    # SHORT             8:54                        08:54                       8:54                        08:54
    # ABBR              8:54 น.                     08:54 น.                    8:54                        08:54
    # LONG              8:54:15 น.                  08:54:15 น.                 8:54:15                     08:54:15
    # FULL              8 นาฬิกา 54 นาที 15 วินาที      08 นาฬิกา 54 นาที 15 วินาที    8h 54m 15s                  08h 54m 15s
    # DATA_SHORT        0854                        0854                        0854                        0854
    # DATA_LONG         085415                      085415                      085415                      085415
    # OFF               /time disabled/
    #endregion

    date_format_types = ('short', 'medium', 'abbr', 'long', 'full', 'data_short', 'data_long', 'off')
    time_format_types = ('short', 'abbr', 'long', 'full', 'data_short', 'data_long', 'off')
    year_systems = ('AD', 'BE')
    
    if yearsystem not in year_systems:
        raise PYRAModuleError("Only 'AD' and 'BE' are accepted as year system.")
    elif date_format_type not in date_format_types:
        raise PYRAModuleError("Only 'short', 'medium', 'abbr', 'long', 'full', 'data_short', 'data_long' or 'off' are accepted as date format.")
    elif time_format_type not in time_format_types:
        raise PYRAModuleError("Only 'short', 'abbr', 'long', 'full', 'data_short', 'data_long' or 'off' are accepted as time format.")

    try:
        # --- สร้างส่วนของวันที่และเวลาในรูปแบบตัวเลขก่อน ---
        if yearsystem == 'BE':
            year_adjustment = 543
        else:
            year_adjustment = 0
        fragment_year = date_and_time.year+year_adjustment
        fragment_month = date_and_time.month
        fragment_date = date_and_time.day
        fragment_weekday = int(date_and_time.strftime("%w"))
        fragment_hour = date_and_time.hour
        fragment_minute = date_and_time.minute
        fragment_second = date_and_time.second

        # --- แปลงส่วนของวันที่และเวลาให้เป็นสตริงที่สามารถนำไปประกอบเป็นสตริงที่ต้องการได้ ---
        # ปีแบบยาว
        part_LongYear = str(fragment_year)
        # ปีแบบสั้น
        part_ShortYear = str(fragment_year % 100)
        # เดือนแบบเต็ม
        if locale == 'TH':
            part_FullMonth = TH_Full_Months[fragment_month-1]
        elif locale == 'EN':
            part_FullMonth = EN_Full_Months[fragment_month-1]
        # เดือนแบบย่อ
        if locale == 'TH':
            part_AbbrMonth = TH_Abbreviated_Months[fragment_month-1]
        elif locale == 'EN':
            part_AbbrMonth = EN_Abbreviated_Months[fragment_month-1]
        # เดือนแบบตัวเลขสองหลัก
        part_LongMonth = str(0)+str(fragment_month) if fragment_month < 10 else str(fragment_month)
        # เดือนแบบตัวเลขหลักเดียว
        part_ShortMonth = str(fragment_month)
        # วันที่แบบเต็ม
        if locale == 'TH':
            part_FullDay = TH_Full_Weekdays[fragment_weekday]
        elif locale == 'EN':
            part_FullDay = EN_Full_Weekdays[fragment_weekday]
        # วันที่แบบย่อ
        if locale == 'TH':
            part_AbbrDay = TH_Abbreviated_Weekdays[fragment_weekday]
        elif locale == 'EN':
            part_FullDay = EN_Full_Weekdays[fragment_weekday]
        # วันที่แบบตัวเลขสองหลัก
        part_LongDay = str(0)+str(fragment_date) if fragment_date < 10 else str(fragment_date)
        # วันที่แบบตัวเลขหลักเดียว
        part_ShortDay = str(fragment_date)
        # ชั่วโมงแบบเต็ม
        part_FullHour = str(fragment_hour)+" นาฬิกา"
        # ชั่วโมงแบบตัวเลขสองหลัก
        part_LongHour = str(0)+str(fragment_hour) if fragment_hour < 10 else str(fragment_hour)
        # ชั่วโมงแบบตัวเลขหลักเดียว
        part_ShortHour = str(fragment_hour)
        # นาทีแบบเต็ม
        part_FullMinute = str(fragment_minute)+" นาที"
        # นาทีแบบตัวเลขสองหลัก
        part_LongMinute = str(0)+str(fragment_minute) if fragment_minute < 10 else str(fragment_minute)
        # นาทีแบบตัวเลขหลักเดียว
        part_ShortMinute = str(fragment_minute)
        # วินาทีแบบเต็ม
        part_FullSecond = str(fragment_second)+" วินาที"
        # วินาทีแบบตัวเลขสองหลัก
        part_LongSecond = str(0)+str(fragment_second) if fragment_second < 10 else str(fragment_second)
        # วินาทีแบบตัวเลขหลักเดียว
        part_ShortSecond = str(fragment_second)

        # --- ประกอบชิ้นส่วนตามการตั้งค่า
        # --- date_format_type, time_format_type, date_delimiter, time_delimiter, leading_zeroes

        if leading_zeroes == False:
            part_Day = part_ShortDay
            part_Month = part_ShortMonth
            part_Hour = part_ShortHour
        else:
            part_Day = part_LongDay
            part_Month = part_LongMonth
            part_Hour = part_LongHour

        if locale == 'TH':
            if date_format_type == 'off':
                dtimestamp = ''
            elif date_format_type == 'short':
                dtimestamp = part_Day+date_delimiter+part_Month+date_delimiter+part_ShortYear
            elif date_format_type == 'medium':
                dtimestamp = part_Day+date_delimiter+part_Month+date_delimiter+part_LongYear
            elif date_format_type == 'abbr':
                dtimestamp = part_Day+" "+part_AbbrMonth
            elif date_format_type == 'long':
                dtimestamp = part_Day+" "+part_FullMonth+" "+part_LongYear
            elif date_format_type == 'full':
                dtimestamp = part_FullDay+"ที่ "+part_ShortDay+" "+part_FullMonth+" "+part_LongYear
            elif date_format_type == 'data_short':
                dtimestamp = part_ShortYear+part_LongMonth+part_LongDay
            elif date_format_type == 'data_long':
                dtimestamp = part_LongYear+part_LongMonth+part_LongDay

            if time_format_type == 'off':
                ttimestamp = ''
            elif time_format_type == 'short':
                ttimestamp = part_Hour+time_delimiter+part_LongMinute
            elif time_format_type == 'abbr':
                ttimestamp = part_Hour+time_delimiter+part_LongMinute+" น."
            elif time_format_type == 'long':
                ttimestamp = part_Hour+time_delimiter+part_LongMinute+time_delimiter+part_LongSecond
            elif time_format_type == 'full':
                ttimestamp = part_FullHour+" "+part_FullMinute+" "+part_FullSecond
            elif time_format_type == 'data_short':
                ttimestamp = part_LongHour+part_LongMinute
            elif time_format_type == 'data_long':
                ttimestamp = part_LongHour+part_LongMinute+part_LongSecond

        return " ".join([ts for ts in [dtimestamp,ttimestamp] if ts])
    except TypeError:
        raise TypeError("ข้อผิดพลาดของระบบวันที่และเวลา : ชนิดข้อมูลที่รับเข้ามาไม่ถูกต้อง")

def getWeekday(d, format_type='full', locale='TH'):
    '''คืนค่าสตริงที่ระบุวันที่ในสัปดาห์ จากข้อมูลวันที่แบบ datetime.date หรือ datetime.datetime ที่ได้รับเข้ามา'''
    if format_type not in ('short', 'abbr', 'full'):
        raise PYRAModuleError("แท็ก format_type ไม่ถูกต้อง ค่าที่สามารถใช้ได้มี 'short', 'abbr', และ 'full'")
    if locale not in ('TH', 'EN'):
        raise PYRAModuleError("แท็ก yearsystem ไม่ถูกต้อง ค่าที่สามารถใช้ได้มี 'AD' แทนปีคริสตศักราช และ 'BE', แทนปีพุทธศักราช")
    
    if format_type == 'short':
        if locale == 'TH':
            return TH_Abbreviated_Weekdays[int(d.strftime("%w"))]
        elif locale == 'EN':
            return EN_Symbol_Weekdays[int(d.strftime("%w"))]
    elif format_type == 'abbr':
        if locale == 'TH':
            return TH_Abbreviated_Weekdays[int(d.strftime("%w"))]
        elif locale == 'EN':
            return EN_Abbreviated_Weekdays[int(d.strftime("%w"))]
    elif format_type == 'full':
        if locale == 'TH':
            return TH_Full_Weekdays[int(d.strftime("%w"))]
        elif locale == 'EN':
            return EN_Full_Weekdays[int(d.strftime("%w"))]
    
def ReformatDate(date_to_reformat, format_type, locale='TH', yearsystem='AD', delimiter='/', leading_zeroes=False):
    '''แปลงค่าประเภทวันที่ (ได้ทั้งชนิดข้อมูล datetime.date และ datetime.datetime) ให้เป็นรูปแบบมาตรฐานที่อ่านได้ง่าย'''
    #region ===== FULL EXAMPLE GUIDE =====
    # UNIVERSAL PARAMETERS as follows: yearsystem='AD', date_delimiter='/', time_delimiter=':'
    #--------------------------------------------------------------------------------------------------------------------------------------
    #                   locale='TH'                 locale='TH'                 locale='EN'                 locale='EN'
    # DATE FORMATS      leading_zeroes=False        leading_zeroes=True         leading_zeroes=False        leading_zeroes=True
    #--------------------------------------------------------------------------------------------------------------------------------------
    # SHORT             5/7/24                      05/07/24                    5/7/24                      05/07/24
    # MEDIUM            5/7/2024                    05/07/2024                  5/7/2024                    05/07/2024
    # ABBR              5 ก.ค. 2024                 05 ก.ค. 2024                5 Jul 2024                  05 Jul 2024
    # LONG              5 กรกฎาคม 2024              05 กรกฎาคม 2024             5 July 2024                 05 July 2024
    # FULL              วันศุกร์ที่ 5 กรกฎาคม 2024       วันศุกร์ที่ 05 กรกฎาคม 2024      Friday, 5 July 2024        Friday, 05 July 2024
    #endregion

    date_format_types = ('short', 'medium', 'abbr', 'long', 'full')
    year_systems = ('AD', 'BE')
    
    if yearsystem not in year_systems:
        raise PYRAModuleError("แท็ก yearsystem ไม่ถูกต้อง ค่าที่สามารถใช้ได้มี 'AD' แทนปีคริสตศักราช และ 'BE', แทนปีพุทธศักราช")
    elif format_type not in date_format_types:
        raise PYRAModuleError("แท็ก format_type ไม่ถูกต้อง ค่าที่สามารถใช้ได้มี 'short', 'medium', 'abbr', 'long' และ 'full'")
    # --- สร้างส่วนของวันที่ในรูปแบบตัวเลขก่อน ---
    fragment_year = str(date_to_reformat.year + 543) if yearsystem == 'BE' else str(date_to_reformat.year)
    fragment_month = f"{date_to_reformat.month:02}" if leading_zeroes else str(date_to_reformat.month)
    fragment_date = f"{date_to_reformat.day:02}" if leading_zeroes else str(date_to_reformat.day)
    fragment_weekday = int(date_to_reformat.strftime("%w"))

    if locale == 'TH':
        if format_type == 'short':
            return fragment_date+delimiter+fragment_month+delimiter+fragment_year[2:]
        elif format_type == 'medium':
            return fragment_date+delimiter+fragment_month+delimiter+fragment_year
        elif format_type == 'abbr':
            return fragment_date+' '+TH_Abbreviated_Months[date_to_reformat.month-1]+' '+fragment_year
        elif format_type == 'long':
            return fragment_date+' '+TH_Full_Months[date_to_reformat.month-1]+' '+fragment_year
        elif format_type == 'full':
            return TH_Full_Weekdays[fragment_weekday]+'ที่ '+fragment_date+' '+TH_Full_Months[date_to_reformat.month-1]+' '+fragment_year
    if locale == 'EN':
        if format_type == 'short':
            return fragment_date+delimiter+fragment_month+delimiter+fragment_year[2:]
        elif format_type == 'medium':
            return fragment_date+delimiter+fragment_month+delimiter+fragment_year
        elif format_type == 'abbr':
            return fragment_date+' '+EN_Abbreviated_Months[date_to_reformat.month-1]+' '+fragment_year
        elif format_type == 'long':
            return fragment_date+' '+EN_Full_Months[date_to_reformat.month-1]+' '+fragment_year
        elif format_type == 'full':
            return EN_Full_Weekdays[fragment_weekday]+', '+fragment_date+' '+EN_Full_Months[date_to_reformat.month-1]+' '+fragment_year

def decodeDateTime(data_to_decode, part_of_datetime, decode_format, yearsystem, locale='TH'):
    '''แปลงประทับเวลาข้อมูลที่พิมพ์ออกจากฟังก์ชัน CreateDataTimestamp (ในรูปแบบ yyyymmdd hhmmss) ให้เป็นรูปแบบที่อ่านได้ตามปกติ'''
    if part_of_datetime not in ('day','month','year','hour','minute','second'):
        raise PYRAModuleError("Incorrect part of datetime tag. Acceptable tags: 'day','month','year','hour','minute','second'.")
    elif locale not in ('TH','EN'):
        raise PYRAModuleError("Incorrect locale tag. Acceptable tags: 'TH','EN'.")
    try:
        source = int(data_to_decode)
    except ValueError:
        raise ValueError("Invalid data to decode. It must be a string using stardard data timestamp format.")
    
    else:
        if part_of_datetime == 'day':
            if not(1 <= source <= 31):
                raise ValueError("Day number must be between 1 to 31.")
            elif decode_format not in ('numbered_day', 'leadingzero_numbered_day'):
                raise PYRAModuleError("Incorrect decoding format tag. Acceptable tags: 'numbered_day', 'leadingzero_numbered_day'.")
            else:
                if decode_format == 'numbered_day':
                    return str(source)
                elif decode_format == 'leadingzero_numbered_day':
                    return str(f"{source:02}")
        elif part_of_datetime == 'month':
            if not(1 <= source <= 12):
                raise ValueError("Day number must be between 1 to 12.")
            elif decode_format not in ('numbered_month', 'leadingzero_numbered_month', 'short_month', 'long_month'):
                raise PYRAModuleError("Incorrect decoding format tag. Acceptable tags: 'numbered_month', 'leadingzero_numbered_month', 'short_month', 'long_month'.")
            else:
                if decode_format == 'numbered_month':
                    return str(source)
                elif decode_format == 'leadingzero_numbered_month':
                    return str(f"{source:02}")
                elif decode_format == 'short_month':
                    return TH_Abbreviated_Months[source-1] if locale == 'TH' else EN_Abbreviated_Months[source-1]
                elif decode_format == 'long_month':
                    return TH_Full_Months[source-1] if locale == 'TH' else EN_Full_Months[source-1]
        elif part_of_datetime == 'year':
            if not(2000 <= source <= 2500):
                raise ValueError("Year number must be in standardized four-digit format (2025) and be between 2000 to 2500.")
            elif decode_format not in ('short_year', 'long_year'):
                raise PYRAModuleError("Incorrect decoding format tag. Acceptable tags: 'short_year', 'long_year'.")
            else:
                if yearsystem == 'BE':
                    source + 543
                if decode_format == 'short_year':
                    return str(source)[2:]
                elif decode_format == 'long_year':
                    return str(source)
        elif part_of_datetime == 'hour':
            if not(0 <= source <= 23):
                raise ValueError("Hour number must be between 0 to 23.")
            elif decode_format not in ('numbered_hour', 'leadingzero_numbered_hour'):
                raise PYRAModuleError("Incorrect decoding format tag. Acceptable tags: 'numbered_hour', 'leadingzero_numbered_hour'.")
            else:
                if decode_format == 'numbered_hour':
                    return str(source)
                elif decode_format == 'leadingzero_numbered_hour':
                    return str(f"{source:02}")
        elif part_of_datetime == 'minute':
            if not(0 <= source <= 59):
                raise ValueError("Minute number must be between 0 to 59.")
            elif decode_format not in ('numbered_minute', 'leadingzero_numbered_minute'):
                raise PYRAModuleError("Incorrect decoding format tag. Acceptable tags: 'numbered_minute', 'leadingzero_numbered_minute'.")
            else:
                if decode_format == 'numbered_minute':
                    return str(source)
                elif decode_format == 'leadingzero_numbered_minute':
                    return str(f"{source:02}")
        elif part_of_datetime == 'second':
            if not(0 <= source <= 59):
                raise ValueError("Second number must be between 0 to 59.")
            elif decode_format not in ('numbered_second', 'leadingzero_numbered_second'):
                raise PYRAModuleError("Incorrect decoding format tag. Acceptable tags: 'numbered_second', 'leadingzero_numbered_second'.")
            else:
                if decode_format == 'numbered_second':
                    return str(source)
                elif decode_format == 'leadingzero_numbered_second':
                    return str(f"{source:02}")

def createDataTimestamp(include_time=True):
    '''สร้างสตริงประทับเวลามาตรฐานในรูปแบบ yyyymmdd-hhmmss จากวันที่และเวลาปัจจุบัน'''
    rawTime = datetime.now()
    # --- สร้างส่วนของวันที่และเวลาในรูปแบบตัวเลขก่อน ---
    rawYear = str(rawTime.year)
    rawMonth = "0"+str(rawTime.month) if rawTime.month < 10 else str(rawTime.month)
    rawDay = "0"+str(rawTime.day) if rawTime.day < 10 else str(rawTime.day)
    DataTimestamp = rawYear+rawMonth+rawDay
    if include_time:
        rawHour = "0"+str(rawTime.hour) if rawTime.hour < 10 else str(rawTime.hour)
        rawMinute = "0"+str(rawTime.minute) if rawTime.minute < 10 else str(rawTime.minute)
        rawSecond = "0"+str(rawTime.second) if rawTime.second < 10 else str(rawTime.second)
        DataTimestamp = DataTimestamp+"-"+rawHour+rawMinute+rawSecond
    return DataTimestamp

def encodeDataTimestamp(date_time, include_time=True):
    rawYear = str(date_time.year)
    rawMonth = "0"+str(date_time.month) if date_time.month < 10 else str(date_time.month)
    rawDay = "0"+str(date_time.day) if date_time.day < 10 else str(date_time.day)
    DataTimestamp = rawYear+rawMonth+rawDay
    if include_time:
        rawHour = "0"+str(date_time.hour) if date_time.hour < 10 else str(date_time.hour)
        rawMinute = "0"+str(date_time.minute) if date_time.minute < 10 else str(date_time.minute)
        rawSecond = "0"+str(date_time.second) if date_time.second < 10 else str(date_time.second)
        DataTimestamp = DataTimestamp+"-"+rawHour+rawMinute+rawSecond
    return DataTimestamp

def decodeDataTimestamp(data_timestamp, include_date=True, include_time=True):
    '''แปลงการจัดรูปแบบวันที่ เวลา หรือวันที่และเวลาที่อยู่ในรูปแบบประทับเวลาข้อมูลมาตรฐาน "yyyymmdd-hhmmss" ให้เป็นวันที่ในรูปแบบที่อ่านได้'''
    if include_date is False and include_time is False:
        raise PYRAModuleError("At least one of these two variables- include_date and include_time- must be True.")
    if len(data_timestamp) not in (6,8,15):
        return ''
        raise ValueError("Invalid data_timestamp.")
    if len(data_timestamp) != 15 and include_date and include_time:
        raise ValueError("Invalid data_timestamp. \nIf you want to decode BOTH date and time, the data_timestamp string length must be of 15 characters according to standard format.")
    if len(data_timestamp) not in (6,15) and include_date==False and include_time:
        raise ValueError("Invalid data_timestamp. \nIf you want to decode ONLY time, the data_timestamp string length must be of 6 characters according to standard format.")
    if len(data_timestamp) not in (8,15) and include_date and include_time==False:
        raise ValueError("Invalid data_timestamp. \nIf you want to decode ONLY date, the data_timestamp string length must be of 8 characters according to standard format.")
    else:
        if len(data_timestamp) == 15:
            rawYear = int(data_timestamp[0:4])
            rawMonth = int(data_timestamp[4:6])
            rawDay = int(data_timestamp[6:8])
            rawHour = int(data_timestamp[9:11])
            rawMinute = int(data_timestamp[11:13])
            rawSecond = int(data_timestamp[13:15])
        elif len(data_timestamp) == 6:
            rawHour = int(data_timestamp[0:2])
            rawMinute = int(data_timestamp[2:4])
            rawSecond = int(data_timestamp[4:6])
        elif len(data_timestamp) == 8:
            rawYear = int(data_timestamp[0:4])
            rawMonth = int(data_timestamp[4:6])
            rawDay = int(data_timestamp[6:8])
        
        if include_date and not include_time:
            DecodedTimestamp = date(rawYear, rawMonth, rawDay)
        if include_date and include_time:
            DecodedTimestamp = datetime(rawYear, rawMonth, rawDay, rawHour, rawMinute, rawSecond)
        if not include_date and include_time:
            DecodedTimestamp = time(rawHour, rawMinute, rawSecond)
        return DecodedTimestamp

def getMilliseconds(get_only_milliseconds=False):
    rawTime = datetime.now()
    rawMinute = rawTime.minute * 60 * 1000
    rawSecond = rawTime.second * 1000
    rawMillisecond = rawTime.microsecond / 1000
    return rawMillisecond if get_only_milliseconds else float(rawMinute+rawSecond+rawMillisecond)

def getMinutesFromTimeDelta(timedelta:timedelta):
    days_part = timedelta.days
    minutes_part = timedelta.seconds//60
    seconds_part = 1
    return (days_part*1440)+minutes_part+seconds_part

def convertToDuration(start:datetime,finish:datetime,output_unit:str="seconds",rounding_mode:str="math",negative_handling:str="normal",reverse:bool=False)-> int:
    '''
    TODO: เพิ่ม handling แท็ก output_unit และ rounding_mode
    คำนวณระยะเวลาในหน่วยวินาที นาที ชั่วโมง หรือวัน จากข้อมูลวันที่และเวลาสองค่า
    '''    

    start_posix = start.timestamp()
    finish_posix = finish.timestamp()

    # Output Unit Conversion
    if output_unit == "seconds":
        result = finish_posix-start_posix
    elif output_unit == "minutes":
        result = (finish_posix-start_posix) / 60.0
    elif output_unit == "hours":
        result = (finish_posix-start_posix) / 60.0 / 60.0
    elif output_unit == "days":
        result = (finish_posix-start_posix) / 60.0 / 60.0 / 24.0
    else:
        raise ValueError(f"Bad tag argument found in -output_unit- : {output_unit}")
    if reverse:
        result * (-1)

    # Negative Duration
    if result >= 0:
        match rounding_mode:
            case 'math':
                return round(result)
            case 'towards_zero':
                return math.floor(result)
            case 'away_from_zero':
                return math.ceil(result)
    else:
        if negative_handling == 'normal':
            match rounding_mode:
                case 'math':
                    return round(result)
                case 'towards_zero':
                    return math.ceil(result)
                case 'away_from_zero':
                    return math.floor(result)
        elif negative_handling == 'zero':
            return 0


def removeDuplicates(list:list) -> list:
    '''Returns a new list as a result of duplicated values elimination from a given list.'''
    result = []
    for n in list:
        if n in result:
            continue
        else:
            result.append(n)
    return result

    



def causePME():
    '''Generates PYRAModuleError exception as a test.'''
    raise PYRAModuleError("You just have voluntarily caused an exception by executing causePME function!")

class PYRAModuleError(Exception):
    '''A man-made Exception subclass perserved for when you are too stupid to remember all nook and cranny of required parameters.'''
    def _render_traceback(self):
        pass