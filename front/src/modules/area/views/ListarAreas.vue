<template>
    <v-container fluid>
        <v-layout>
            <v-flex xs10>
                <v-data-table
                    :headers="header"
                    :items="areas"
                >
                    <template
                        v-slot:items="props"
                    >
                        <td>{{ props.index + 1 }}</td>
                        <td>
                            <a
                                :href="getAreaUrl(props.item.id)">
                                {{ props.item.nome }}
                            </a>
                        </td>
                    </template>
                </v-data-table>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'ListarAreas',
    data() {
        return {
            header: [
                {
                    text: '#',
                    align: 'left',
                    sortable: false,
                    value: 'numero',
                },
                {
                    text: 'nome',
                    value: 'nome',
                },
            ],
            areas: [],
        };
    },
    computed: {
        ...mapGetters({
            listaAreas: 'area/areas',
        }),
    },
    watch: {
        listaAreas() {
            this.areas = this.listaAreas;
        },
    },
    created() {
        this.buscarAreas();
    },
    methods: {
        ...mapActions({
            buscarAreas: 'area/buscarAreas',
        }),
        getAreaUrl(id) {
            return `area/${id}`;
        },
    },
};
</script>
