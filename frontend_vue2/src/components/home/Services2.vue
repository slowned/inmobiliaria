<template>
  <div class="block galleryBlock">
      <v-row>
        <v-col v-for="item in items" :key="item.id" class="d-flex child-flex" cols="6" sm="4">
          <v-hover v-slot="{ hover }">
              <v-card
                flat tile class="d-flex"
                :class="{ 'on-hover': hover }"
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
  </div>
</template>

<script>
export default {
  name: "Services2",
  data() {
    return {
      items: [
        {
          id: 1,
          title: "Tasaciones",
          src: 'https://la.network/wp-content/uploads/2019/09/mario-home.jpg'
        },
        {
          id: 2,
          title: "Loteos",
          src: 'https://la.network/wp-content/uploads/2019/09/mario-home.jpg'
        },
        {
          id: 3,
          title: "Consorcios",
          src: 'https://la.network/wp-content/uploads/2019/09/mario-home.jpg'
        }
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

.v-card:not(.on-hover) {
  opacity: 0.6;
 }
</style>
