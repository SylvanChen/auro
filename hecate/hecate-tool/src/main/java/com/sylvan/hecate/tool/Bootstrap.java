package com.sylvan.hecate.tool;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/** @author sylvan */
@SpringBootApplication
public class Bootstrap {
  public static void main(String[] args) {
    SpringApplication springApplication = new SpringApplication(Bootstrap.class);
    System.out.println(Bootstrap.class.getName());
    springApplication.run(args);
  }
}