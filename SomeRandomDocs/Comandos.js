function ActualizarFechasProximasEjecucionLimpiar(fecha = ""){
    for (let i = 0; i < 200; i++){
        if(document.getElementById('listaAMsDisparoPendientes_Date_fecha_'+String(i))){
            almacenarCambioFecha('listaAMsDisparoPendientes', i, 'fecha', fecha);
            Mantum_Util.value('listaAMsDisparoPendientes_Date_fecha_'+String(i),fecha);
        }
        if(document.getElementById('listaAMsDisparo_Date_fecha_'+String(i))){
            almacenarCambioFecha('listaAMsDisparo', i, 'fecha', fecha);
            Mantum_Util.value('listaAMsDisparo_Date_fecha_'+String(i),fecha);
        }
    }
}
ActualizarFechasProximasEjecucionLimpiar();