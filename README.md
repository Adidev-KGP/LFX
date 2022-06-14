This pytest code simply does a REST call to the ODL controller and checks the response code is 200 OK and the response body contains the string "ietf-restconf".

The original test was written in robot framework and this pytest code is doing the same test.

Link to the robot framework testing code - https://git.opendaylight.org/gerrit/gitweb?p=integration/test.git;a=blob;f=csit/suites/integration/basic/restconf_modules.robot;h=b4811b1caff8999c9c5c3c11eca9f904d1bc65f4;hb=HEAD




To run both the test methods:

running test module test_status_code: ```py.test -k status_code -v```

running test module test_responsebody: ```py.test -k responsebody -v```


