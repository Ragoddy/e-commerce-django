// js for main fron markets
// js for Orders Home

function operateOrderFormatter(value, row, index) {
    return [
      '<a class="status_order btn btn-info btn-circle" href="javascript:void(0)" title="Cambiar Estado">',
      '<i class="fa fa-retweet"></i>',
      '</a>  ',
      '<a class="detail_order btn btn-primary btn-circle" href="javascript:void(0)" title="Detalle del pedido">',
      '<i class="fa fa-list-alt"></i>',
      '</a>  '
    ].join('')
}

window.operateOrderEvents = {
    'click .status_order': function (e, value, row, index) {                
        var $order_id = $('#order_id');
        var id = row.UUID;
        var status = row.status_order;
        $order_id.val(id);
        
        if(status == 0){
            $('#option_cancel').button('toggle');
        }else if(status == 1){
            $('#option_received').button('toggle');
        }else if(status == 2){
            $('#option_progress').button('toggle');
        }else{
            $('#option_closed').button('toggle');
        }

        $('#modal_order_status').modal("show");
    },
    'click .detail_order': function (e, value, row, index) {
        
        var $id_market = $('#id_market').val();
        var $token = $('#token').val();
        var $name = $('#name');
        var $phone = $('#phone');
        var $address = $('#address');
        var $complement_address = $('#complement_address');
        var $total_price = $('#total_price');
        var $comments = $('#comments');
        var $payment_method = $('#payment_method');

        var total_price = new Intl.NumberFormat().format(row.total_price)
        var pay_method = (row.payment_method == 1) ? "Efectivo" : "Datafono";
        var url = "/api/v1/orders/products/" + row.UUID + "/";
        var $table_products_list = $("#table_products_list");

        
        $name.val(row.name_client);
        $phone.val(row.phone);
        $address.val(row.address);
        $complement_address.val(row.complement_address);
        $total_price.val("$ " + total_price);
        $comments.val(row.comments);
        $payment_method.val(pay_method);

        //execute busy loading              
        $.busyLoadFull("show",{ 
            animation: "slide",
            spinner: "circles", 
            text: "Cargando pedido, Por favor espere...", 
            background: "rgba(0, 51, 101, 0.7)",
            fontSize: "1.6rem"
        }); 
        
        //execute api for products
        axios.get(url, {headers: {"Authorization" : "Token " + $token}})
        .then((response) => {
            $("#table_products_list tbody").empty();
            $.each(response.data.data, function( key, value ) {
                var number = new Intl.NumberFormat().format(value.total_price)
                $table_products_list.append('<tr><th scope="row">'+ value.amount +'</th><td>' + value.product_name + '</td><td>$' + number + '</td></tr>');
            });
            $('#modal_order_detail').modal("show");
            $.busyLoadFull("hide");
        }, (error) => {
            alert(error);
            $.busyLoadFull("hide");
        });        
        
    }
}

function totalPriceOrderFormatter(value, row) {
    var number = new Intl.NumberFormat().format(value)
    return '<p class="text-center">$ ' + number + '</p>'
}
function payMethodOrderFormatter(value, row) {
    if (row.payment_method == 1){
        return '<p class="text-center"> <i class="fa fa-money-bill"></i> Efectivo</p>'
    }else{
        return '<p class="text-center"> <i class="fa fa-mobile"></i> Datafono</p>'
    }
}
function statusOrderFormatter(value, row) {
    if (value== 0){
        return '<p class="text-center"> <i class="text-danger fa fa-flag-checkered"></i> - Cancelado</p>'
    }else  if (value == 1){
        return '<p class="text-center"> <i class="text-success fa fa-flag"></i> - Recibido</p>'
    }else  if (value == 2){
        return '<p class="text-center"> <i class="text-info fa fa-flag"></i> - Procesando</p>'
    }else  if (value == 3){
        return '<p class="text-center"> <i class="text-primary fa fa-flag-checkered"></i> - Enviado</p>'
    }
}
function dateOrderFormatter(value, row) {
    return moment(value).format('DD/MM/YYYY HH:mm:ss');
}


function refreshOrderCount(){
    var $id_market = $('#id_market').val();
    var $token = $('#token').val();
    var $oActive = $('#order_active');
    var $oHistoric = $('#order_historic');
    var url = "/api/v1/orders/count/" + $id_market + "/";
    axios.get(url, {headers: {"Authorization" : "Token " + $token}})
    .then((response) => {
        $oActive.html(response.data.data.orders_count);
        $oHistoric.html(response.data.data.orders_historic_count)
    }, (error) => {
        alert(error);
    });
}

$(document).ready(function() {        

    $("#btn_send_status").click(function(){
        var $token = $('#token').val();
        var $cancel = $("#rd_cancel:checked").val();
        var $received = $("#rd_received:checked").val();
        var $progress = $("#rd_progress:checked").val();
        var $closed = $("#rd_closed:checked").val();
        var $order_id = $('#order_id').val();
        var $dataTableOrders = $('#dataTableOrders');
        var url = "/api/v1/orders/status/";
    
        var status_result = 1;
        if($cancel > 0){
            status_result = 0;
        }else if($received > 0){
            status_result = 1;
        }else if($progress > 0){
            status_result = 2;
        }else if($closed > 0){
            status_result = 3;
        }
        
        //create dataset
        var data = {
            order_id: $order_id,
            status_order: status_result
        }
        //execute api                
        axios.post(url, data, {headers: {"Authorization" : "Token " + $token}})
        .then((response) => {
            if(response.data.success == true){
                $dataTableOrders.bootstrapTable('refresh');
            }else{          
                alert("Se genero un error al cambiar el estado, por favor intente nuevamente");
            }

            refreshOrderCount();
        }, (error) => {
            alert(error);
        });

    });


    function refreshOrders(){
        if($('#id_market').val()> 0){
            $('#dataTableOrders').bootstrapTable('refresh');
            refreshOrderCount();
        }
    }

    var myDataLoading = setInterval(refreshOrders, 10000);
    
   
});
  