<html>
  <head>
     <title>
        Тестируем PHP
     </title>
  </head>
  <body>

  <?php
    echo '<h1>Hello, world!</h1>';
  ?>

  <br />

  <?php
    $colors = array("red", "green", "blue", "yellow");

    foreach ($colors as $value) {
        echo "* $value <br />\n";
    }
  ?>

  </body>
</html>

