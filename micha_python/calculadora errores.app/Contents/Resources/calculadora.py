from Cocoa import *
from Foundation import NSObject
import math

class calculatorControler(NSWindowController):
    displaya = objc.IBOutlet()
    displayb = objc.IBOutlet()
    
    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)
        
        # Start the counter
        self.valoresfuncion  = 0
        self.errorfuncion    = 0
        self.quedisplay      = True
        self.AoB             = True
        self.coma            = False
        self.multiplicadorA  = 1
        self.multiplicadorB  = 1
        self.variableA       = 0
        self.variableB       = 0
        self.errorA          = 0
        self.errorB          = 0
        self.numeronumeros   = 0
        self.operacion       = 0
        self.salidavariable  = 0
        self.salidaerror     = 0
        self.displayA        = 0
        self.displayB        = 0
        self.multiplicadorAA   = True
        self.multiplicadorAB   = True
    
        
    @objc.IBAction
    def botonerre_(self, sender):
        if self.quedisplay == True:
            self.quedisplay = False

        else:
            self.quedisplay = True
        self.numeronumeros = 0
        self.coma            = False
    
    @objc.IBAction
    def botoncoma_(self, sender):
        self.coma = True
        self.numeronumeros = 1
    
    @objc.IBAction
    def boton0_(self, sender):
        numero=0
        if self.quedisplay == True:
            if self.AoB == True:
                if self.coma ==True:
                    self.variableA = self.variableA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
                else:
                    self.variableA = (self.variableA * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
            else:
                if self.coma ==True:
                    self.variableB = self.variableB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableB
                
                else:
                    self.variableB = (self.variableB * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableB

        else:
            if self.AoB == True:
                if self.coma ==True:
                    self.errorA = self.errorA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorA
                
                else:
                    self.errorA = (self.errorA * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorA
        
            else:
                if self.coma ==True:
                    self.errorB = self.errorB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorB
                
                else:
                    self.errorB = (self.errorB * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorB


        self.updateDisplay()
    
    @objc.IBAction
    def boton1_(self, sender):
        numero=1
        if self.quedisplay == True:
            if self.AoB == True:
                if self.coma ==True:
                    self.variableA = self.variableA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
                else:
                    self.variableA = (self.variableA * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
            else:
                if self.coma ==True:
                    self.variableB = self.variableB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableB
                
                else:
                    self.variableB = (self.variableB * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableB

        else:
            if self.AoB == True:
                if self.coma ==True:
                    self.errorA = self.errorA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorA
                
                else:
                    self.errorA = (self.errorA * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorA
        
            else:
                if self.coma ==True:
                    self.errorB = self.errorB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorB
                
                else:
                    self.errorB = (self.errorB * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorB

        self.updateDisplay()

    @objc.IBAction
    def boton2_(self, sender):
        numero=2
        if self.quedisplay == True:
            if self.AoB == True:
                if self.coma ==True:
                    self.variableA = self.variableA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
                else:
                    self.variableA = (self.variableA * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
            else:
                if self.coma ==True:
                    self.variableB = self.variableB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableB
                
                else:
                    self.variableB = (self.variableB * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableB

        else:
            if self.AoB == True:
                if self.coma ==True:
                    self.errorA = self.errorA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorA
                
                else:
                    self.errorA = (self.errorA * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorA
        
            else:
                if self.coma ==True:
                    self.errorB = self.errorB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorB
                
                else:
                    self.errorB = (self.errorB * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorB
        self.updateDisplay()

    @objc.IBAction
    def boton3_(self, sender):
        numero=3
        if self.quedisplay == True:
            if self.AoB == True:
                if self.coma ==True:
                    self.variableA = self.variableA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
                else:
                    self.variableA = (self.variableA * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
            else:
                if self.coma ==True:
                    self.variableB = self.variableB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableB
                
                else:
                    self.variableB = (self.variableB * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableB

        else:
            if self.AoB == True:
                if self.coma ==True:
                    self.errorA = self.errorA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorA
                
                else:
                    self.errorA = (self.errorA * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorA
        
            else:
                if self.coma ==True:
                    self.errorB = self.errorB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorB
                
                else:
                    self.errorB = (self.errorB * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorB

        self.updateDisplay()

    @objc.IBAction
    def boton4_(self, sender):
        numero=4
        if self.quedisplay == True:
            if self.AoB == True:
                if self.coma ==True:
                    self.variableA = self.variableA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
                else:
                    self.variableA = (self.variableA * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
            else:
                if self.coma ==True:
                    self.variableB = self.variableB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableB
                
                else:
                    self.variableB = (self.variableB * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableB

        else:
            if self.AoB == True:
                if self.coma ==True:
                    self.errorA = self.errorA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorA
                
                else:
                    self.errorA = (self.errorA * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorA
        
            else:
                if self.coma ==True:
                    self.errorB = self.errorB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorB
                
                else:
                    self.errorB = (self.errorB * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorB
        self.updateDisplay()

    @objc.IBAction
    def boton5_(self, sender):
        numero=5
        if self.quedisplay == True:
            if self.AoB == True:
                if self.coma ==True:
                    self.variableA = self.variableA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
                else:
                    self.variableA = (self.variableA * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
            else:
                if self.coma ==True:
                    self.variableB = self.variableB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableB
                
                else:
                    self.variableB = (self.variableB * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableB

        else:
            if self.AoB == True:
                if self.coma ==True:
                    self.errorA = self.errorA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorA
                
                else:
                    self.errorA = (self.errorA * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorA
        
            else:
                if self.coma ==True:
                    self.errorB = self.errorB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorB
                
                else:
                    self.errorB = (self.errorB * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorB

        self.updateDisplay()

    @objc.IBAction
    def boton6_(self, sender):
        numero=6
        if self.quedisplay == True:
            if self.AoB == True:
                if self.coma ==True:
                    self.variableA = self.variableA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
                else:
                    self.variableA = (self.variableA * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
            else:
                if self.coma ==True:
                    self.variableB = self.variableB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableB
                
                else:
                    self.variableB = (self.variableB * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableB

        else:
            if self.AoB == True:
                if self.coma ==True:
                    self.errorA = self.errorA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorA
                
                else:
                    self.errorA = (self.errorA * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorA
        
            else:
                if self.coma ==True:
                    self.errorB = self.errorB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorB
                
                else:
                    self.errorB = (self.errorB * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorB
        self.updateDisplay()

    @objc.IBAction
    def boton7_(self, sender):
        numero=7
        if self.quedisplay == True:
            if self.AoB == True:
                if self.coma ==True:
                    self.variableA = self.variableA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
                else:
                    self.variableA = (self.variableA * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
            else:
                if self.coma ==True:
                    self.variableB = self.variableB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableB
                
                else:
                    self.variableB = (self.variableB * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableB

        else:
            if self.AoB == True:
                if self.coma ==True:
                    self.errorA = self.errorA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorA
                
                else:
                    self.errorA = (self.errorA * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorA
        
            else:
                if self.coma ==True:
                    self.errorB = self.errorB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorB
                
                else:
                    self.errorB = (self.errorB * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorB
        self.updateDisplay()

    @objc.IBAction
    def boton8_(self, sender):
        numero=8
        if self.quedisplay == True:
            if self.AoB == True:
                if self.coma ==True:
                    self.variableA = self.variableA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
                else:
                    self.variableA = (self.variableA * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
            else:
                if self.coma ==True:
                    self.variableB = self.variableB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableB
                
                else:
                    self.variableB = (self.variableB * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableB

        else:
            if self.AoB == True:
                if self.coma ==True:
                    self.errorA = self.errorA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorA
                
                else:
                    self.errorA = (self.errorA * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorA
        
            else:
                if self.coma ==True:
                    self.errorB = self.errorB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorB
                
                else:
                    self.errorB = (self.errorB * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorB


        self.updateDisplay()

    @objc.IBAction
    def boton9_(self, sender):
        numero=9
        if self.quedisplay == True:
            if self.AoB == True:
                if self.coma ==True:
                    self.variableA = self.variableA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
                else:
                    self.variableA = (self.variableA * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableA
                    
                    
            else:
                if self.coma ==True:
                    self.variableB = self.variableB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayA = self.variableB
                
                else:
                    self.variableB = (self.variableB * 10) + numero
                    self.numeronumeros += 1
                    self.displayA = self.variableB

        else:
            if self.AoB == True:
                if self.coma ==True:
                    self.errorA = self.errorA + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorA
                
                else:
                    self.errorA = (self.errorA * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorA
        
            else:
                if self.coma ==True:
                    self.errorB = self.errorB + numero * math.pow(0.1,self.numeronumeros)
                    self.numeronumeros += 1
                    self.displayB = self.errorB
                
                else:
                    self.errorB = (self.errorB * 10) + numero
                    self.numeronumeros += 1
                    self.displayB = self.errorB

        self.updateDisplay()

    @objc.IBAction
    def botonmultiplicacion_(self, sender):
        self.operacion = 1
        self.AoB     = False
        self.coma      = False
        self.quedisplay      = True
        self.displayB = 0
    
    @objc.IBAction
    def botonsuma_(self, sender):
        self.operacion = 2
        self.AoB     = False
        self.coma      = False
        self.quedisplay      = True
        self.displayB = 0
    
    @objc.IBAction
    def botondividir_(self, sender):
        self.operacion = 3
        self.AoB     = False
        self.coma      = False
        self.quedisplay      = True
        self.displayB = 0
    
    @objc.IBAction
    def botonelevar_(self, sender):
        self.operacion = 4
        self.AoB     = False
        self.coma      = False
        self.quedisplay      = True
        self.displayB = 0
    
    @objc.IBAction
    def botonresta_(self, sender):
        self.operacion = 5
        self.AoB     = False
        self.coma      = False
        self.quedisplay      = True
        self.displayB = 0

    @objc.IBAction
    def botonborrar_(self, sender):
        if self.quedisplay == True:
            if self.AoB == True:
                if self.variableA==0:
                    self.coma= False
                    return
                if type(self.variableA) == int:
                    self.variableA= self.variableA/10
                    self.numeronumeros -=1
                    self.displayA = self.variableA
                else:
                    self.variableA= int((math.pow(10,self.numeronumeros)*self.variableA))
                    self.variableA=self.variableA/10
                    self.variableA=float(self.variableA)
                    self.numeronumeros -=1
                    self.variableA=self.variableA/pow(10,self.numeronumeros)
                    self.displayA = self.variableA
            else:
                if self.variableB==0:
                    self.coma= False
                    return
                if type(self.variableB) == int:
                    self.variableB= self.variableB/10
                    self.displayA = self.variableB
                    self.numeronumeros -=1
                    self.displayA = self.variableB
                else:
                    self.variableB= int((math.pow(10,self.numeronumeros)*self.variableB))
                    self.variableB=self.variableB/10
                    self.variableB=float(self.variableB)
                    self.numeronumeros -=1
                    self.variableB=self.variableB/pow(10,self.numeronumeros)
                    self.displayA = self.variableB
        else:
            if self.AoB == True:
                if self.errorA==0:
                    self.coma= False
                    return
                if type(self.errorA) == int:
                    self.errorA= self.errorA/10
                    self.numeronumeros -=1
                    self.displayB = self.errorA
                
                else:
                    self.errorA= int((math.pow(10,self.numeronumeros)*self.errorA))
                    self.errorA=self.errorA/10
                    self.errorA=float(self.errorA)
                    self.numeronumeros -=1
                    self.errorA=self.errorA/pow(10,self.numeronumeros)
                    self.displayB = self.errorA
            else:
                if self.errorB==0:
                    self.coma= False
                    return
                if type(self.errorB) == int:
                    self.errorB= self.errorB/10
                    self.numeronumeros -=1
                    self.displayB = self.errorB
                
                else:
                    self.errorB= int((math.pow(10,self.numeronumeros)*self.errorB))
                    self.errorB=self.errorB/10
                    self.errorB=float(self.errorB)
                    self.numeronumeros -=1
                    self.errorB=self.errorB/pow(10,self.numeronumeros)
                    self.displayB = self.errorB



        self.updateDisplay()



    @objc.IBAction
    def botoncambiosigno_(self, sender):
        if self.AoB == True:
            self.multiplicadorA *= -1
    
        else:
            self.multiplicadorB *= -1
            
        self.updateDisplay()
            
                

    @objc.IBAction
    def botonigualdad_(self, sender):
        if self.variableB != 0 :
            self.variableA = self.variableA * self.multiplicadorA
            self.variableB = self.variableB * self.multiplicadorB
            if self.operacion == 1:
                self.salidavariable = self.variableA * self.variableB
                self.salidaerror=math.pow(self.variableB * self.errorA,2)+math.pow(self.variableA * self.errorB,2)
                self.salidaerror=math.sqrt(self.salidaerror)
                self.displayA=self.salidavariable
                self.displayB=self.salidaerror
                self.updateDisplay()
            
            elif self.operacion == 2:
                self.salidavariable = self.variableA + self.variableB
                self.salidaerror=math.pow(self.errorA,2)+math.pow(self.errorB,2)
                self.salidaerror=math.sqrt(self.salidaerror)
                self.displayA=self.salidavariable
                self.displayB=self.salidaerror
                self.updateDisplay()
            
            elif self.operacion == 3:
                self.salidavariable = self.variableA / self.variableB
                self.salidaerror=math.pow(self.variableA / self.variableA,2)*(math.pow(self.errorA / self.variableA,2)+math.pow(self.errorB / self.errorB,2))
                self.salidaerror=math.sqrt(self.salidaerror)
                self.displayA=self.salidavariable
                self.displayB=self.salidaerror
                self.updateDisplay()
            
            elif self.operacion == 4:
                self.salidavariable = math.pow(self.variableA , self.variableB )
                self.salidaerror=math.pow(self.variableA,self.variableB)*self.errorA/self.variableA
                self.salidaerror=math.sqrt(self.salidaerror)
                self.displayA=self.salidavariable
                self.displayB=self.salidaerror
                self.updateDisplay()
            
            elif self.operacion == 5:
                self.salidavariable = self.variableA - self.variableB
                self.salidaerror=math.pow(self.errorA,2)+math.pow(self.errorB,2)
                self.salidaerror=math.sqrt(self.salidaerror)
                self.displayA=self.salidavariable
                self.displayB=self.salidaerror
                self.updateDisplay()
        self.valoresfuncion  = 0
        self.errorfuncion    = 0
        self.quedisplay      = True
        self.AoB             = True
        self.coma            = False
        self.variableA       = 0
        self.variableB       = 0
        self.errorA          = 0
        self.errorB          = 0
        self.numeronumeros   = 0
        self.operacion       = 0
        self.salidavariable  = 0
        self.salidaerror     = 0
        self.multiplicadorA   = True
        self.multiplicadorB   = True
        self.multiplicadorAA   = True
        self.multiplicadorAB   = True

    def updateDisplay(self):
        if self.AoB == True:
            disa=self.displayA*self.multiplicadorA
       
        else:
            disa=self.displayA*self.multiplicadorB

        self.displaya.setStringValue_(disa)
        self.displayb.setStringValue_(self.displayB)

if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    
    # Initiate the contrller with a XIB
    viewController = calculatorControler.alloc().initWithWindowNibName_("calculadora")
    
    # Show the window
    viewController.showWindow_(viewController)
    
    # Bring app to top
    NSApp.activateIgnoringOtherApps_(True)
    
    from PyObjCTools import AppHelper
    AppHelper.runEventLoop()























