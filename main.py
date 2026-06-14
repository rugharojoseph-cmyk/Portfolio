import flet as ft

def main(page: ft.Page):
    page.title = "Rugharo Joseph Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.window_width = 1300
    page.window_height = 800
    
    content = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )
    
    # HOME SECTION
    def show_home(e=None):
        content.controls.clear()
        content.controls.append(
            ft.Column(
                controls=[
                    ft.Image(
                        src="profile.jpg",
                        width=180,
                        height=180,
                        border_radius=90
                    ),
                    ft.Text(
                        "RUGHARO JOSEPH",
                        size=35,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Text(
                        "Student Number: 225057506 | Role: UI/UX Lead (Group 10)",
                        size=18,
                        weight=ft.FontWeight.W_500
                    ),
                    ft.Text(
                        "Computer Programming I - Semester 1, 2026",
                        size=18
                    ),
                    ft.Divider(),
                    ft.Text(
                        "Welcome to my professional individual web portfolio.\n"
                        "This interactive portal showcases my specific technical contributions, "
                        "learning milestones, and evidence archives for the development of "
                        "'Blast Assist'—a safety-first blasting management application.",
                        size=16,
                        text_align=ft.TextAlign.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    # TIMELINE SECTION
    def show_timeline(e):
        content.controls.clear()
        content.controls.extend([
            ft.Text(
                "PROJECT TIMELINE (UI/UX CONTRIBUTIONS)",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Week 1: Foundations & Architecture Alignment", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Collaborated with the Project Manager and Leads to translate the engineering problem statement into structural app views. Mapped out the dual-persona operational pathways for Mining Engineers and Community gateways.")
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Week 2: Material Design & HIG Wireframing", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Drafted low-fidelity UI layouts using Google Material Design standards for Android and Apple's Human Interface Guidelines (HIG). Prioritized clean spatial scaling for data entry inputs.")
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Week 3: High-Stress Field Optimization UI", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Refined touch-target dimensions and implemented a high-contrast visual palette to guarantee layout visibility for field workers operating in extreme outdoor glare or wearing thick safety gloves.")
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Week 4: Usability Engineering & Interface Prototyping", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Constructed high-fidelity components for the Predictive Blasting Engine dashboard and automated alerting screens. Tested navigation hierarchy flow via simulation runs to reduce manual entry error rates.")
                    ])
                )
            )
        ])
        page.update()

    # TECHNICAL BLOG SECTION (Fixed math markdown rendering argument)
    def show_blog(e):
        content.controls.clear()
        content.controls.extend([
            ft.Text(
                "TECHNICAL BLOG: CONFIDENCE IN CONCEPTS",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Predictive Blasting Engine Calculations", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("To substitute error-prone manual calculations in mining environments, the core engine automates key dimensions using geological constants adjusted for specific landscapes (Rocky $K=0.35$ vs. Mountainous $K=0.50$):"),
                        ft.Markdown(
                            value=(
                                r"**1. Burden Calculation ($B$):**" "\n"
                                r"$$B = d \times K$$" "\n"
                                r"*(Where $d$ is hole diameter in mm and $K$ represents the Burden geological factor)*" "\n\n"
                                r"**2. Hole Spacing ($S$):**" "\n"
                                r"$$S = B \times 1.25$$" "\n"
                                r"*(Based on standard equilateral field patterns for rock fragmentation)*" "\n\n"
                                r"**3. Target Hole Depth ($H$):**" "\n"
                                r"$$H = B \times 2.5$$"
                            ),
                            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                            selectable=True
                        ),
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Civil & Mining Cost Analysis Formulations", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("In civil and mining automation systems, structured predictive resource tracking is vital. Total project overhead constraints and material procurement estimates are modeled using strict mathematical matrices:"),
                        ft.Markdown(
                            value=r"$$Total\_Cost = \sum_{i=1}^{71} (Q_i \times P_i) + Overheads$$",
                            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                            selectable=True
                        ),
                        ft.Text("Where Q represents explosive or asset volumetric quantities, and P dictates pricing thresholds adjusted against volatile material constants.", size=12, italic=True)
                    ])
                )
            )
        ])
        page.update()

    # MATLAB ACHIEVEMENT HUB SECTION (Fixed fit property)
    def show_matlab(e):
        content.controls.clear()
        content.controls.append(
            ft.Text(
                "MATLAB ACHIEVEMENT HUB (Course Progress Verification)",
                size=30,
                weight=ft.FontWeight.BOLD
            )
        )
        
        certificates = [
            "matlab1.png", "matlab2.png", "matlab3.png", 
            "matlab4.png", "matlab5.png", "matlab6.png"
        ]
        
        grid = ft.GridView(
            expand=True,
            runs_count=2,
            max_extent=400,
            child_aspect_ratio=1.4,
            spacing=15,
            run_spacing=15
        )
        
        for cert in certificates:
            grid.controls.append(
                ft.Card(
                    content=ft.Container(
                        padding=10,
                        content=ft.Image(
                            src=cert,
                            fit=ft.ImageFit.CONTAIN if hasattr(ft, "ImageFit") else "contain"
                        )
                    )
                )
            )
        content.controls.append(grid)
        page.update()

    # GITHUB EVIDENCE SECTION (Fixed fit properties)
    def show_github(e):
        content.controls.clear()
        img_fit = ft.ImageFit.CONTAIN if hasattr(ft, "ImageFit") else "contain"
        
        content.controls.extend([
            ft.Text(
                "GITHUB EVIDENCE & COMPLIANCE ARCHIVE",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Developer Profile & Repository Context", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("GitHub Username: rugahrojoseph-cmyk", size=16),
                        ft.Text("Repository Assignment: waardeakawa-sys/UNAM-I3691CP-GROUP-10-TOOLBOX", size=14, color=ft.Colors.BLUE_800, weight=ft.FontWeight.BOLD),
                        ft.Text("Note: Production logs exist entirely within the designated group organization hub outlined below:", size=13, italic=True),
                        ft.Row([
                            ft.Container(content=ft.Image(src="github/commit1.png", fit=img_fit), width=450),
                            ft.Container(content=ft.Image(src="github/repo.png", fit=img_fit), width=450),
                        ], spacing=15, wrap=True, alignment=ft.MainAxisAlignment.CENTER)
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Commit Records & Contribution Graph Logs", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("Verified records demonstrating individual branch commits integrated into the Group 10 master codebase ecosystem:"),
                        ft.Row([
                            ft.Container(content=ft.Image(src="github/commit2.png", fit=img_fit), width=450),
                            ft.Container(content=ft.Image(src="github/contributions.png", fit=img_fit), width=450),
                        ], spacing=15, wrap=True, alignment=ft.MainAxisAlignment.CENTER)
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Pull Requests & Peer Code Review Audit", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("Verification windows tracking proposed structural visual components, state controls, and team cross-review integrations:"),
                        ft.Row([
                            ft.Container(content=ft.Image(src="github/pr1.png", fit=img_fit), width=450),
                            ft.Container(content=ft.Image(src="github/pr2.png", fit=img_fit), width=450),
                        ], spacing=15, wrap=True, alignment=ft.MainAxisAlignment.CENTER)
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Individual Impact Summary", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text(
                            "My contributions as UI/UX Lead directly fixed human-error calculation risks inherent in manual workflows. "
                            "By implementing structural, high-contrast inputs designed for high-glare environments, "
                            "the interface enables operators to reliably input mathematical parameters—such as rock density, "
                            "blast area sizes, and water content metrics—without layout clipping or accidental inputs. "
                            "This design guarantees operational security, speed, and safety in high-stress engineering environments.",
                            size=14
                        )
                    ])
                )
            )
        ])
        page.update()

    # CONTACT SECTION
    def show_contact(e):
        content.controls.clear()
        content.controls.extend([
            ft.Text(
                "CONTACT SPECIFICATIONS",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            ft.Divider(),
            ft.Text("Full Name: Rugharo Joseph", size=16),
            ft.Text("Student Number: 225057506", size=16),
            ft.Text("Email: rugharojoseph@gmail.com", size=16),
            ft.Text("Verified Github Profile: rugahrojoseph-cmyk", size=16)
        ])
        page.update()

    # SIDEBAR CONTROL PANELS (Upgraded to modern ft.Button syntax to stop warnings)
    sidebar = ft.Container(
        width=220,
        bgcolor=ft.Colors.BLUE_100,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text(
                    "PORTFOLIO",
                    size=28,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Divider(),
                ft.Button("Home", on_click=show_home, width=180),
                ft.Button("Timeline", on_click=show_timeline, width=180),
                ft.Button("Technical Blog", on_click=show_blog, width=180),
                ft.Button("MATLAB Hub", on_click=show_matlab, width=180),
                ft.Button("GitHub Evidence", on_click=show_github, width=180),
                ft.Button("Contact", on_click=show_contact, width=180)
            ],
            spacing=10
        )
    )
    
    page.add(
        ft.Row(
            controls=[
                sidebar,
                ft.VerticalDivider(),
                ft.Container(
                    content=content,
                    expand=True,
                    padding=20
                )
            ],
            expand=True
        )
    )
    show_home()

# Upgraded target app execution wrapper to run() to completely eliminate remaining warnings
ft.run(
    main,
    assets_dir="assets"
)