#install.packages("memoise")
library(reticulate)
library(shiny)
library(reticulate)


source_python("algoritmos_.py")


shinyServer(function(input, output) {
  
  #Gradient Descent para el problema cuadrático
  QP_GD_Calc<-eventReactive(input$BFQ, {
    inputEcStr<-input$BFQ[1]
    Q<-input$Q_FQ[1]
    x0<-input$x0_FQ[1]
    c<-input$c_FQ[1]
    tolerance<-input$E_FQ[1]
    max_iterations<-input$N_FQ[1]
    step_size_type<-input$at_FQ[1]
    step_size_value<-input$a_FQ[1]
    outs<-gradient_descent_quadratic(Q,c,x0,tolerance,max_iterations,step_size_type,step_size_value)
    outs
  })
  
  #Gradient Descent para la RosenBrocks Function
  FR_GD_Calc<-eventReactive(input$BFR, {
    inputEcStr<-input$BFR[1]
    x0<-input$x0_FR[1]
    E<-input$E_FR[1]
    N<-input$N_FR[1]
    a<-input$a_FR[1]
    outs<-RF_GD(x0,E,N,a)
    outs
  })
  
  #Render QP_GD
  output$salidaFQ<- renderTable({
    QP_GD_Calc()
  })
  
  #Render FR_GD
  output$salidaFR<- renderTable({
    FR_GD_Calc()
  })
})


