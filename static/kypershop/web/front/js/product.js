// js for products
function operateProductFormatter(value, row, index) {
    return [
      '<a class="disabled_product btn btn-info btn-circle btn-sm" href="javascript:void(0)" title="Deshabilitar producto">',
      '<i class="fa fa-minus-square"></i>',
      '</a>  ',
      '<a class="edit_product btn btn-primary btn-circle btn-sm" href="javascript:void(0)" title="Editar producto">',
      '<i class="fa fa-edit"></i>',
      '</a>  ',
      '<a class="remove_product btn btn-danger btn-circle btn-sm" href="javascript:void(0)" title="Eliminar producto">',
      '<i class="fa fa-trash-alt"></i>',
      '</a>'
    ].join('')
}

window.operateProductEvents = {
    'click .disabled_product': function (e, value, row, index) { 
               
        $('#modal_product_stock').modal("show");
    },
    'click .edit_product': function (e, value, row, index) {
        var $creation_date = $('#creation_date');
        var $title = $('#title');
        var $description = $('#description');
        var $price = $('#price');
        var $available = $('#available');
        var $status = $('#status');

        var number = new Intl.NumberFormat().format(row.price)
        console.log(number);
        $creation_date.val(moment(row.creation_date).format('DD/MM/YYYY HH:mm'));
        $title.val(row.title);
        $description.val(row.description);
        $price.val(number);
        $available.val((row.available == 1) ? "Sí" : "No");
        $status.val((row.status == 1) ? "Activo" : "Inactivo");

        $('#modal_product_edit').modal("show");
    },
    'click .remove_product': function (e, value, row, index) {

        $('#modal_product_remove').modal("show");
    }
}

function imageProductFormatter(value, row) {    
    return '<img class="text-center" src="' + row.image + '" alt="'+ row.title +'" height="45" width="65">'
}

function priceProductFormatter(value, row) {
    var number = new Intl.NumberFormat().format(row.price)
    return '<p class="text-center">$ ' + number + '</p>'
}
function availableProductFormatter(value, row) {
    if (row.available == 1){
        return '<p class="text-center"> Sí</p>'
    }else{
        return '<p class="text-center"> No</p>'
    }
}
function statusProductFormatter(value, row) {
    if (row.status == 1){
        return '<p class="text-center"> Activo</p>'
    }else{
        return '<p class="text-center"> InActivo</p>'
    }
}
function dateProductFormatter(value, row) {
    return moment(value).format('DD/MM/YYYY HH:mm');
}



$(document).ready(function() {            

    $("#btn_send_status").click(function(){
        // var $token = $('#token').val();
        // var $cancel = $("#rd_cancel:checked").val();
        // var $received = $("#rd_received:checked").val();
        // var $progress = $("#rd_progress:checked").val();
        // var $closed = $("#rd_closed:checked").val();
        // var $order_id = $('#order_id').val();
        // var $dataTableOrders = $('#dataTableOrders');
        // var url = "/api/v1/orders/status/";
    
        // var status_result = 1;
        // if($cancel > 0){
        //     status_result = 0;
        // }else if($received > 0){
        //     status_result = 1;
        // }else if($progress > 0){
        //     status_result = 2;
        // }else if($closed > 0){
        //     status_result = 3;
        // }
        
        // //create dataset
        // var data = {
        //     order_id: $order_id,
        //     status_order: status_result
        // }
        // //execute api                
        // axios.post(url, data, {headers: {"Authorization" : "Token " + $token}})
        // .then((response) => {
        //     if(response.data.success == true){
        //         $dataTableOrders.bootstrapTable('refresh');
        //     }else{          
        //         alert("Se genero un error al cambiar el estado, por favor intente nuevamente");
        //     }

        //     refreshOrderCount();
        // }, (error) => {
        //     alert(error);
        // });

    });
    
   
});