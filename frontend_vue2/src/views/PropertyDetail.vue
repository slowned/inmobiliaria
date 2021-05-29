<template>
  <div v-if="property">
    <h3>Detalle de la propiedad</h3>
    <span>Direccion {{property.address}}</span>
    <span>Precio ${{property.price}}</span>
    <span>Descripcion: {{property.description}}</span>
  </div>
</template>

<script>

import PropertyService from "@/services/PropertyService.js"
 
export default {
  props: ['id'],
  data() {
    return {
      property: null
    }
  },
  created() {
    PropertyService.getProperty(this.id)
      .then((response) => {
        this.property = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style>
</style>
