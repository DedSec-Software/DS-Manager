from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Table,
    TableStyle,
    Image,
    Spacer,
    Indenter,
)
from time import ctime
from threading import Thread


class AccountReport(BaseDocTemplate):
    def __init__(
        self, filename, entries, balance, date_from, date_to, level, **kwargs,
    ):
        super().__init__(filename, page_size=A4, _pageBreakQuick=0, **kwargs)
        self.income, self.expense = entries
        self.cash_bal, self.main_acc_bal, self.building_acc_bal = balance
        self.date_from = date_from
        self.date_to = date_to
        self.level = level
        self.leftMargin = 2
        self.bottomMargin = 2
        self.topMargin = 2
        self.rightMargin = 2
        self.width, self.height = A4

        self.style = getSampleStyleSheet()
        self.style.add(
            ParagraphStyle(
                name="customTitle",
                parent=self.style["Title"],
                fontName="Times-Roman",
                leading=15,
                spaceAfter=2,
            )
        )

        self.style.add(
            ParagraphStyle(
                name="trusty", fontName="Times-Roman", fontSize=10, leading=12
            )
        )
        self.style.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY))
        self.style.add(ParagraphStyle(name="Right", alignment=TA_RIGHT))
        self.title_style = self.style["customTitle"]
        self.trusty_style = self.style["trusty"]

        # Setting up the frames, frames are use for dynamic content not fixed page elements
        page_table_frame = Frame(
            6 * cm,
            10,
            self.width - 6 * cm - 10,
            self.height - 4 * cm,
            id="small_table",
            showBoundary=1,
        )

        # Creating the page templates
        page_temp = PageTemplate(
            id="Page", frames=[page_table_frame], onPage=self.add_default_info
        )

        self.addPageTemplates([page_temp])

        story = []
        story.append(Indenter(100))
        story.append(Spacer(1, 5))
        ptext = (
            f"<para align=right><font size=9>Report Generate at:&nbsp; &nbsp;"
            f"<font bgcolor={colors.cornsilk}>{ctime()}</font></font></para>"
        )
        story.append(Paragraph(ptext, self.style["Right"]))
        story.append(Spacer(1, 20))
        story.append(Indenter(-70))

        ptext = (
            f"<font size=11>Report Generate from &nbsp;&nbsp;<font color='darkblue'>{self.date_from}</font>"
            f"&nbsp;&nbsp; to &nbsp;&nbsp;<font color='darkblue'>{self.date_to}</font></font>"
        )
        story.append(Paragraph(ptext, self.style["Justify"]))
        story.append(Spacer(1, 20))

        ptext = "<para align=left><font color='#191970' fontsize=12><u>Entries of Income</u></font></para>"
        story.append(Paragraph(ptext, self.title_style))
        story.append(Indenter(-30))
        story.append(Spacer(1, 12))

        table_header, col_width = self.sorted_format()

        table_data = [table_header]

        for entry in self.income:
            table_data.append(entry)

        story.append(
            Table(
                table_data,
                repeatRows=1,
                colWidths=col_width,
                style=TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.lavender),
                        ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
                    ]
                ),
            )
        )

        story.append(Indenter(30))
        story.append(Spacer(1, 40))
        ptext = "<para align=left><font color='#191970' fontsize=12><u>Entries of Expense</u></font></para>"
        story.append(Paragraph(ptext, self.title_style))
        story.append(Indenter(-30))
        story.append(Spacer(1, 12))

        table_data = [table_header]
        for entry in self.expense:
            table_data.append([entry[0], entry[1], f"(-{entry[2]})"])

        story.append(
            Table(
                table_data,
                repeatRows=1,
                colWidths=col_width,
                style=TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.lavender),
                        ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
                    ]
                ),
            )
        )

        story.append(Spacer(1, 40))
        story.append(Indenter(50))

        data = [
            [
                self.create_text("Total Main Account Bank Balance", 12, True),
                f"{self.main_acc_bal[1]} Rs",
            ],
            [
                self.create_text("Total Building Account Bank Balance", 12, True),
                f"{self.building_acc_bal[1]} Rs",
            ],
            [
                self.create_text("Total Cash Balance", 12, True),
                f"{self.cash_bal[1]} Rs",
            ],
        ]

        col_width = [250, 80]
        story.append(
            Table(
                data,
                colWidths=col_width,
                style=TableStyle(
                    [
                        ("BACKGROUND", (-1, 0), (-1, -1), colors.bisque),
                        ("BACKGROUND", (-1, 1), (-1, 1), colors.blanchedalmond),
                        ("ALIGN", (0, 0), (0, -1), "CENTER"),
                    ]
                ),
            )
        )

        self.build(story)

    def sorted_format(self):
        if self.level == "level 1":
            table_header = [
                self.create_text("Transaction Type", bold=True),
                self.create_text("Source", bold=True),
                self.create_text("Money", bold=True),
            ]
            col_width = [150, 130, 80]
            self.income = self.sorting(self.income)
            self.expense = self.sorting(self.expense)
        else:
            table_header = [
                self.create_text("Transaction Type", bold=True),
                self.create_text("Detailed", bold=True),
                self.create_text("Date", bold=True),
                self.create_text("Source", bold=True),
                self.create_text("Money", bold=True),
            ]
            col_width = [100, 80, 80, 80, 60]
        return table_header, col_width

    def create_text(self, text, size=9, bold=False):

        if bold:
            return Paragraph(
                """<font size={size}><b>{text}</b></font>""".format(
                    size=size, text=text
                ),
                self.style["Normal"],
            )
        return Paragraph(
            """<font size={size}>{text}</font>""".format(size=size, text=text),
            self.style["Normal"],
        )

    def on_first_page(self, canvas, doc):
        canvas.saveState()
        # Add the logo and other default stuff
        self.add_default_info(canvas, doc)

        canvas.restoreState()

    def add_default_info(self, canvas, doc):
        canvas.saveState()
        logo_frame = Frame(0, doc.height - 3.8 * cm, 3.5 * cm, 4 * cm)
        logo_frame.add(self.get_register_logo(), canvas)

        header_frame = Frame(4 * cm, doc.height - 3 * cm, doc.width - 5 * cm, 3 * cm)
        header_frame.add(self.get_header(), canvas)

        trusty_frame = Frame(0, 0, 6 * cm, doc.height - 4 * cm)
        trusty_frame.add(self.get_trusty(), canvas)
        canvas.drawImage("inc/logo_watermark.png", 267, 300, 200, 236)
        canvas.setFont("Helvetica", 7)
        canvas.drawString(4, 4, "Report Generated by: DS MANAGER")

        canvas.restoreState()

    def get_header(self):
        header_text = """
                    <font fontsize=24><font color="green">MUHIYIDEEN JUMMA MOSQUE</font></font>
                    <br></br>
                    <font size=12>
                    YONAKAPURA, DICKWELLA
                    <br></br>
                    Reg, No : R/387/MR/14
                    <br></br>
                    T.P No: 0412257401 | e-mail:<font color="blue"> dickwellamj@gmail.com</font>
                    </font>
                """
        header_para = Paragraph(header_text, self.title_style)
        return header_para

    def get_register_logo(self):
        register_logo = Image("inc/logo_head.png", 3 * cm, 3.5 * cm)
        return register_logo

    def get_trusty(self):
        trusty_text = """
                    <b><i>PRESIDENT</i>
                    <br/>
                    MR. M.S. IMTHIYAS AHAMED</b>
                    <br/>
                    Proprietor: “Glass house” Dickwella
                    <br/>
                    TP: (+94) 72 225616
                    <br/><br/>

                    <b><i>VICE PRESIDENT</i>
                    <br/>
                    AL-HAJ A.S.A. RILWAN</b>
                    <br/>
                    Proprietor: “Safra Garment” Dickwella
                    <br/>
                    TP: (+94) 77 3723242
                    <br/><br/>

                    <b><i>SECRETARY</i>
                    <br/>
                    AS-SHEIKH M.S.M. RIFHAN BA, MBA</b>
                    <br/>
                    Dip.in. Adv.Eng, Dip.in Ports Ops.Mng,
                    <br/>
                    Justice of peace(Whole island)
                    <br/>
                    Asst.Manger (HR/Admin),
                    <br/>
                    Sri Lanka ports Authority
                    <br/>
                    TP: (+94) 77 3927571, (+94) 71 5329249
                    <br/>
                    e-mail: <font color="blue">msmrifhan@gmail.com</font>,
                    <font color="blue">rifhan@slpa.lk</font>
                    <br/><br/>

                    <b><i>ASST. SECRETARY</i>
                    <br/>
                    MR. M.C.M. MUKARRAM, BA</b>
                    <br/>
                    Dip.in Edu, SLEAS(Rtd .Principal)
                    <br/>
                    Justice of peace(Whole island)
                    <br/>
                    TP: (+94) 77 2191190
                    <br/>
                    e-mail: <font color="blue">mukarram2013@gmail.com</font>
                    <br/><br/>

                    <b><i>TREASURER</i>
                    <br/>
                    AL-HAJ M.N. HASHAN</b>
                    <br/>
                    Proprietor: "Colombo Hardware Stores" Dickwella
                    <br/>
                    TP: (+94) 77 7909369
                    <br/><br/>

                    <b><i>ASST. TREASURER</i>
                    <br/>
                    AL-HAJ M.H.A. MUNAS</b>
                    <br/>
                    Proprietor: "Shukriya Industries" Dickwella
                    <br/>
                    TP: (+94) 77 7856587
                    <br/><br/>

                    <b><i>CO-ORDINATOR</i>
                    <br/>
                    Deshamaniya, Deshakeerthi
                    ASH SHEIKH M.S.M IHRAZ, B.A</b>
                    <br/>
                    Dip.in Adv.Eng, Dip.in Psy & Couns.
                    <br/>
                    Principal: Nooraniyyah Arabic College, Matara
                    <br/>
                    Member of ACJU (Matara Distric)
                    <br/>
                    TP: (+94) 71 3332019, (+94) 767232019
                    <br/>
                    e-mail: <font color="blue">ihrazfathi333@gmail.com</font>
                """
        trusty_para = Paragraph(trusty_text, self.trusty_style)
        return trusty_para

    def sorting(self, entries):
        sorted_entries = []
        for entry in entries:
            index = None
            for row in sorted_entries:
                if entry[0] == row[0] and entry[1] == row[1]:
                    index = sorted_entries.index(row)
                    break

            if index is not None:
                sorted_entries[index][2] += entry[2]
            else:
                sorted_entries.append(list(entry))

        return sorted_entries
