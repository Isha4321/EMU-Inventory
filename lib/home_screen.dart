import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {

  var wtController = TextEditingController();
  var ftController = TextEditingController();
  var inController = TextEditingController();
  var result = "";
  var bgColor = Colors.blueAccent.shade100;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Heathy Body'),
          centerTitle: true,
        ),
        body: Container(
          color: bgColor ,
          child: Center(
            child: SingleChildScrollView(
              child: Container(
                width: 300,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text('BMI' , style: TextStyle(
                        fontSize: 34, fontWeight: FontWeight.w600
                    ),),
                    SizedBox(height: 25),
                    TextField(
                      controller: wtController,
                      decoration: InputDecoration(
                          label: Text('Enter your Weight(in kgs)'),
                          prefixIcon: Icon(Icons.monitor_weight_outlined)
                      ),
                      keyboardType: TextInputType.number,
                    ),
                    SizedBox(height: 15 ),
                    TextField(
                      controller: ftController,
                      decoration: InputDecoration(
                          label: Text('Enter your Height(in feets)'),
                          prefixIcon: Icon(Icons.height_outlined)
                      ),
                      keyboardType: TextInputType.number,
                    ),
                    SizedBox(height: 15 ),
                    TextField(
                      controller: inController,
                      decoration: InputDecoration(
                          label: Text('Enter your Height(in cms)'),
                          prefixIcon: Icon(Icons.height)
                      ),
                      keyboardType: TextInputType.number,
                    ),
                    SizedBox(height: 30),
                    ElevatedButton(onPressed: (){

                      var wt = wtController.text.toString();
                      var ft = ftController.text.toString();
                      var inch = inController.text.toString();

                      if(wt!="" && ft!="" && inch!=""){
                       // BMI Calculation
                        var iWt = int.parse(wt);
                        var iFt = int.parse(ft);
                        var iInch = int.parse(inch);

                        var tInch = (iFt*12) + iInch;
                        var tCm = tInch*2.54;
                        var tM = tCm/100;

                        var bmi = iWt/(tM*tM);
                        var msg = "";
                        if(bmi>25)
                          {
                              msg = "You're OverWeight !!";
                              bgColor = Colors.red.shade200;
                          }
                        else if(bmi<18){
                            msg = "You're UnderWeight !!";
                            bgColor = Colors.yellow.shade200;
                        }
                        else
                          {
                             msg = "You're Healthy :) ";
                             bgColor = Colors.green.shade200;
                          }


                        setState(() {
                          result = "$msg \n Your BMI is:${bmi.toStringAsFixed(2)}";
                        });
                      }
                      else
                        {
                          setState(() {
                            result = "Please fill all blanks !!";
                          });
                        }

                    }, child: Text('Calculate')),
                    SizedBox(height: 10),

                    Text(result,style: TextStyle(fontSize: 20),)
                  ],
                ),
              ),
            ),
          ),
        )
    );
  }
}
