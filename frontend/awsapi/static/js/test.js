
function initiate_test() {
    console.log("Test suite start!");

    /************************************************
    // Table rendering tests.
    *************************************************/
    // Render table
    var test_table_id = "table-1";
    var test_container_id = "container-1";
    var rows = [
        ["Behzad", "Dastur"],
        ["John", "Doe"]
    ];
    render_table(["Last name", "First name"], rows, "container-1", test_table_id);

    var data = ["David", "Smith"];

    render_table_insert_row(data, test_table_id);




    var attributes = [{
	    "id": "table-1"
    }];
    headers = ["Last Name", "First Name"];

    new_table = new Table(attributes, test_container_id);
    new_table.insert_rows(rows, headers);
    new_table.insert_rows([["Oak", "Durban"]]);


}
