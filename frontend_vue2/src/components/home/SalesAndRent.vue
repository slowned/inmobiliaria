<template>
  <div class="block galleryBlock">
    <v-container fluid>
      <v-row>
        <v-col v-for="item in items" :key="item.id" class="d-flex child-flex" cols="6">
          <v-hover v-slot="{ hover }">
              <v-card
                flat tile class="d-flex"
                :class="{ 'on-hover': hover }"
                :height="200"
                to="propiedades"
              >
              <v-img :src="item.src" aspect-ratio="1" class="grey lighten-2">
                <template v-slot:placeholder>
                  <v-row class="fill-height ma-0" align="center" justify="center">
                    <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                  </v-row>
                </template>
                <div class="center">
                  <h3 class="cardTitle">{{ item.title }}</h3>
                </div>
              </v-img>
            </v-card>
          </v-hover>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "SalesAndRent",
  data() {
    return {
      items: [
        {
          id: 1,
          title: "Alquileres",
          src: 'https://picsum.photos/350/165?random'
        },
        {
          id: 2,
          title: "Ventas",
          src: 'https://picsum.photos/350/165?random'
        },
      ],
      transparent: 'rgba(255, 255, 255, 0)',
    };
  }
};
</script>

<style scoped>
.cardTitle {
    text-align: center;
    font-size: 35px;
    font-weight: bold;
    font-family: cursive;
}
.center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.v-card {
  transition: opacity .4s ease-in-out;
}

/* .v-card:not(.on-hover) {
  opacity: 0.6;
 } */
</style>
