// js for main fron markets
// js for products
function operateProductFormatter(value, row, index) {
    return [
      '<a class="enable btn btn-info btn-circle btn-sm" href="javascript:void(0)" title="Deshabilitar producto">',
      '<i class="fa fa-minus-square"></i>',
      '</a>  ',
      '<a class="enable btn btn-primary btn-circle btn-sm" href="javascript:void(0)" title="Editar producto">',
      '<i class="fa fa-edit"></i>',
      '</a>  ',
      '<a class="remove btn btn-danger btn-circle btn-sm" href="javascript:void(0)" title="Eliminar producto">',
      '<i class="fa fa-trash-alt"></i>',
      '</a>'
    ].join('')
}

window.operateProductEvents = {
    'click .enable': function (e, value, row, index) {
        alert('You click like action, row: ' + JSON.stringify(row))
    },
    'click .remove': function (e, value, row, index) {
        
    }
}

function imageProductFormatter(value, row) {    
    return '<img class="text-center" src="' + row.image + '" alt="'+ row.title +'" height="45" width="65">'
}

function priceProductFormatter(value, row) {
    var number = new Intl.NumberFormat('nu', { style: 'currency', currency: 'COP' }).format(row.price)
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



// js for Orders Home
function operateOrderFormatter(value, row, index) {
    return [
      '<a class="enable btn btn-info btn-circle" href="javascript:void(0)" title="Cambiar Estado">',
      '<i class="fa fa-retweet"></i>',
      '</a>  ',
      '<a class="enable btn btn-primary btn-circle" href="javascript:void(0)" title="Detalle del pedido">',
      '<i class="fa fa-list-alt"></i>',
      '</a>  '
    ].join('')
}

window.operateOrderEvents = {
    'click .enable': function (e, value, row, index) {
        alert('You click like action, row: ' + JSON.stringify(row))
    },
    'click .remove': function (e, value, row, index) {
        
    }
}

function totalPriceOrderFormatter(value, row) {
    var number = new Intl.NumberFormat().format(value)
    return '<p class="text-center">$ ' + number + '</p>'
}
function payMethodOrderFormatter(value, row) {
    if (row.status == 1){
        return '<p class="text-center"> <i class="fa fa-money-bill"></i> Efectivo</p>'
    }else{
        return '<p class="text-center"> <i class="fa fa-mobile"></i> Datafono</p>'
    }
}
function statusOrderFormatter(value, row) {
    if (value== 0){
        return '<p class="text-center"> Cancelado</p>'
    }else  if (value == 1){
        return '<p class="text-center"> Recibido</p>'
    }else  if (value == 2){
        return '<p class="text-center"> Procesando</p>'
    }else  if (value == 3){
        return '<p class="text-center"> Enviado</p>'
    }
}
function dateOrderFormatter(value, row) {
    return moment(value).format('DD/MM/YYYY HH:mm');
}
$(document).ready(function() {    

   
});
  