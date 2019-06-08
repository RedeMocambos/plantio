<template>
    <v-container
        fluid
        grid-list-xs
    >
        <v-layout
        >
            <v-flex
                xs12
            >
                <v-tabs>
                    <v-tabs-slider color=""></v-tabs-slider>
                    <v-tab
                        href="#dados"
                    >
                        <v-icon
                            class="pa-2"
                        >
                            notes
                        </v-icon>
                        dados da área
                    </v-tab>
                    <v-tab
                        href="#desenho"
                    >
                        <v-icon
                            class="pa-2"
                        >
                            grid_on
                        </v-icon>
                        desenho
                    </v-tab>
                    <v-tab
                        href="#plantios"
                    >
                        <v-icon
                            class="pa-2"
                        >
                            local_florist
                        </v-icon>
                        plantios
                    </v-tab>
                    <v-tab-item
                        :value="'dados'"
                    >
                        <v-flex
                            xs12
                        >
                            <v-card>
                                <v-card-title class="subheading">
                                    Dados da área
                                </v-card-title>
                                <p>
                                    {{ dadosArea.nome }}
                                </p>
                                <p>
                                    Localidade: <a :href="getLocalidadeUrl(dadosArea.localidade_id)">{{ dadosArea.localidade }}</a>
                                </p>
                                <p>
                                    Microclima: {{ dadosArea.microclima }}
                                </p>
                                <p>
                                    Dimensões:
                                </p>
                                <p>
                                    {{ dadosArea.comprimento }}m x {{ dadosArea.largura }}m
                                </p>
                                <p>
                                    {{ dadosArea.dimensao }}m2
                                </p>
                            </v-card>
                        </v-flex>
                    </v-tab-item>
                    <v-tab-item
                        :value="'desenho'"
                    >
                        <v-flex
                            xs12
                        >
                            <v-card>
                                <v-card-title class="subheading">
                                    Desenho de área
                                </v-card-title>
                                <Grid
                                    :dimensions="dimensions"
                                />
                            </v-card>
                        </v-flex>
                    </v-tab-item>
                    <v-tab-item
                        :value="'plantios'"
                    >
                        Plantios
                        <listar-plantios/>
                    </v-tab-item>
                </v-tabs>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>

import { mapActions, mapGetters } from 'vuex';
import Grid from '@/modules/desenho/Grid';
import ListarPlantios from '@/modules/plantio/views/ListarPlantios';

export default {
    name: 'VisualizarArea',
    components: {
        Grid,
        ListarPlantios,
    },
    data() {
        return {
            dimensions: {
                sizeX: 0,
                sizeY: 0,
            },
        };
    },
    computed: {
        ...mapGetters({
            dadosArea: 'area/area',
        }),
    },
    watch: {
        dadosArea() {
            this.dimensions.sizeX = this.dadosArea.largura;
            this.dimensions.sizeY = this.dadosArea.comprimento;
        },
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarArea(this.$route.params.id);
        }
    },
    methods: {
        ...mapActions({
            buscarArea: 'area/buscarArea',
        }),
        getLocalidadeUrl(id) {
            return `/localidade/${id}`;
        },
    },
};
</script>
