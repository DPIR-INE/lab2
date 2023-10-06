#install.packages("memoise")
library(shiny)
library(shinydashboard)

# Define UI for application that draws a histogram
dashboardPage(
  dashboardHeader(title = "Laboratorio #2"),
  dashboardSidebar(
    sidebarMenu(
      menuItem("Funcion Cuadrática", tabName = "FQ"),
      menuItem("RosenBrocks Function", tabName = "FR")
    )
  ),
  dashboardBody(
    tabItems(
      tabItem("FQ",
              h1("Funcion Cuadrática"),
              box(textInput("Q_FQ", "Matriz Q"),
                  textInput("c_FQ", "c"),
                  textInput("x0_FQ", "X inicial"),
                  textInput("E_FQ", "Tolerancia máxima"),
                  textInput("N_FQ", "Iteraciones máximas"),
                  radioButtons('at_FQ','Step size',c('Exacto'='0',
                                                     'Constante'='1',
                                                     'Variable'='2')),
                  textInput("a_FQ", "Tamaño de step size constante")),
              actionButton("BFQ", "Gradient Descent"),
              tableOutput("salidaFQ")),
      
      tabItem("FR",
              h1("RosenBrocks Function"),
              box(textInput("x0_FR", "X inicial"),
                  textInput("E_FR", "Tolerancia máxima"),
                  textInput("N_FR", "Iteraciones máximas"),
                  textInput("a_FR", "Step Size")),
              actionButton("BFR", "Gradient Descent"),
              tableOutput("salidaFR"))
    )
  )
)