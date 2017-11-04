package com.test.a;

interface Animal2
{
   public void eat();
   public void travel();
   final int CONST1 = 1000;
   final String CONST_STR = "Const example!!!!";
}

public class Animal
{
   int foo;
   String bar;

   Animal()
   {
      this.foo = 123123;
      this.bar = "asdasdasd";
   }
}

public class Dog extends Animal implements Animal2{
   String breed;
   int age;
   String color;
   private float ddddd;
   private static String finderaaaa;

   int barking(int a,int b) {
   }

   void hungry() {
   }

   void sleeping() {
   }
}

public class Bird extends Animal implements a,b,c{
   String breed;
   int age;
   String color;

   int flying(int a,int b) {
   }

   void hungry() {
   }

   void sleeping() {
   }
}


public class HelloWorld {
    public static void main( String[] args ) {
        System.out.println( "Hello World!" );
        System.exit( 0 ); //success
    }
}